# Use slim Python base
FROM python:3.11.3-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install pip dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y git && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache && \
    apt-get remove -y git && apt-get autoremove -y

# Copy project files into the container
COPY . .

# Expose all used ports
EXPOSE 8000 
EXPOSE 7860
EXPOSE 7861
EXPOSE 8001


# Default command (can override this when running)
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
