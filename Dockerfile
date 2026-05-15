FROM python:3.14.3-slim

WORKDIR /app

# First, copy requirements to leverage Docker's cache for faster builds
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Explicitly copy the current directory contents into the container's work directory
COPY . /app

# Start the FastAPI server using uvicorn
# server:app refers to the 'app' object inside the 'server.py' file
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
