# Use official Python 3.11.3 base image
FROM python:3.11.3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port (adjust if using Streamlit, FastAPI, etc.)
EXPOSE 7860 
EXPOSE 8000
# Use 8000 if FastAPI, 7860 if Gradio

# Command to run app (replace with your actual command)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11.3-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default: start FastAPI
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
