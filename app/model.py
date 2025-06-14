import pickle
import re
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
import joblib


def clean_text(text):
    text = text.lower()
    return re.sub(r"[^\w\s]", "", text)


def load_all():
    with open("model/ensemble_model.pkl", "rb") as f:
        model = joblib.load(f)
    with open("model/vectorizer.pkl", "rb") as f:
        vectorizer = joblib.load(f)
    with open("model/le.pkl", "rb") as f:
        label_encoder = joblib.load(f)
    return model, vectorizer, label_encoder


def predict_label(text, model, vectorizer, label_encoder):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)
    return label_encoder.inverse_transform(pred)[0]
