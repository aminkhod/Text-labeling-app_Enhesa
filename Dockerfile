FROM python:3.11.3-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default: start FastAPI
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
