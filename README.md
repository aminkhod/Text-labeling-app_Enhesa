# README

## Setup Instructions

To create the conda environment for this project, run:

```
conda env create -f environment.yml
```

This will install all required dependencies as specified in the `environment.yml`


## Building and Running

Build the image
```
docker build -t text-classifier-app .
```

Run FastAPI app
```
docker run -p 8000:8000 text-classifier-app
```

Run Gradio app

```
docker run -p 7860:7860 text-classifier-app python app/gradio_app.py
```

# REST API Usage Guide

## Overview

This project provides a REST API for text prediction. You can send a POST request with your text, and the API will return a prediction.

---

## Endpoint

- **URL:** `http://localhost:8000/predict`
- **Method:** `POST`
- **Content-Type:** `application/json`

---

## Request Format

Send a JSON object with a `text` field:

```json
{
  "text": "your text to analyze"
}
```

---

## Example Using PowerShell

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/predict" `
  -Method Post `
  -Body '{"text": "your text to analyze"}' `
  -ContentType "application/json"
```

---

## Example Using `curl`

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "your text to analyze"}'
```

---

## Response

The API will return a JSON response with the prediction, for example:

```json
{
  "prediction": "label_name"
}
```

---

