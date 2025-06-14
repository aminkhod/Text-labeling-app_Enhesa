# Text Labeling App (Enhesa)

This project is a text classification application built with Python. It provides both a REST API and a user interface for predicting labels for input text using machine learning models.

---

## Features

- **Text classification** using multiple machine learning models (Logistic Regression, Random Forest, Gradient Boosting, Linear SVC, and an ensemble Voting Classifier)
- **REST API** for programmatic access (built with FastAPI)
- **Web UI** for interactive use (built with Gradio)
- **Model saving/loading** for reproducible results

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Text-labeling-app_Enhesa.git
cd Text-labeling-app_Enhesa
```

### 2. Create the Conda Environment

```bash
conda env create -f environment.yml
conda activate text-labeling-app
```

### 3. Install Additional Dependencies (if needed)

If you use pip, install requirements with:

```bash
pip install -r requirements.txt
```

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
- The UI will open in your browser.

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

## Saving and Loading Models

Models are saved using `joblib`:

```python
import joblib

# Save a model
joblib.dump(model, 'model_filename.pkl')

# Load a model
model = joblib.load('model_filename.pkl')
```

---

## Contributing

Feel free to open issues or submit pull requests!

---

## License

This project is licensed under