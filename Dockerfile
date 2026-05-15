FROM python:3.14.3-slim

WORKDIR /app

# First, copy requirements to leverage Docker's cache for faster builds
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /app/server.py

# Start the FastAPI server using uvicorn
# server:app refers to the 'app' object inside the 'server.py' file
# Reload watches for any python changes inside app folder
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
