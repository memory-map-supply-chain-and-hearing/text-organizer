FROM python:3.14.3-slim

WORKDIR /backend

# First, copy requirements to leverage Docker's cache for faster builds
COPY requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the backend application code and tests
# This copies server.py, routes/, and tests/ directly into /backend
COPY backend .

# Start the FastAPI server using uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
