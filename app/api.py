from fastapi import FastAPI
from pydantic import BaseModel

from app.model import load_all, predict_label

app = FastAPI()
model, vectorizer, label_encoder = load_all()


class TextRequest(BaseModel):
    text: str


@app.post("/predict")
def predict(request: TextRequest):
    prediction = predict_label(request.text, model, vectorizer, label_encoder)
    return {"prediction": prediction}
