# Text Labeling App (Enhesa)

This project is a text classification application built with Python. It provides both a REST API and a user interface for predicting labels for input text using machine learning models.

---

## Features

- **Text classification** using multiple machine learning models ( Random Forest, Gradient Boosting, Linear SVC, and an ensemble Voting Classifier)
- **REST API** for programmatic access (built with FastAPI)
- **Web UI** for interactive use (built with Gradio)
- **Model saving/loading** for reproducible results

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aminkhod/Text-labeling-app_Enhesa.git
cd Text-labeling-app_Enhesa
```

### 2. Create the Conda Environment

```bash
conda env create -f environment.yml
conda activate enhesa
```

### 3. Install Additional Dependencies (if needed)

If you use pip, install requirements with:

```bash
pip install -r requirements.txt
```

---

## Docker

### Build and Run
```bash
docker build -t text-classifier-app .
```

### FastAPI app
#### To run the standard FastAPI app:
```bash
docker run -p 8000:8000 text-classifier-app

```
- The API will be available at: `http://localhost:8000`
#### To run the RAG FastAPI app
```bash
docker run -p 8001:8001 text-classifier-app python -m uvicorn app.rag_api:app --host 0.0.0.0 --port 8001
```
- Wait for downloading and loading the model (~500m)

- The API will be available at: `http://localhost:8001`

### Gradio demo
#### To run the Gradio demo (standard):
```bash
docker run -p 7860:7860 text-classifier-app python app/gradio_app.py

```
- The UI will open in your browser at : `http://localhost:7860`.

#### To run the RAG Gradio demo:


```bash
docker run -p 7861:7861 text-classifier-app python app/rag_gradio_app.py
```
- Wait for downloading and loading the model (~500m)

- The UI will open in your browser at : `http://localhost:7861`.


---

## Running the Application

### Start the REST API

```bash
uvicorn app:app --reload
```
- The API will be available at: `http://localhost:8000`

### Start the Gradio Web UI

```bash
python gradio_app.py
```
- The UI will open in your browser at : `http://localhost:7860`.

---

## Using the REST API

### Endpoint

- **POST** `/predict`
- **Content-Type:** `application/json`

#### Request Example

```json
{
  "text": "your text to analyze"
}
```

#### PowerShell Example

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/predict" `
  -Method Post `
  -Body '{"text": "your text to analyze"}' `
  -ContentType "application/json"
```

---

#### Response Example

```bash
prediction
----------
cult
```

#### curl Example

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "your text to analyze"}'
```

#### Response Example

```json
{
  "prediction": "label_name"
}
```

---
