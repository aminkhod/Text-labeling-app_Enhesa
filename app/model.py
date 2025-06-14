import pickle
import re


def clean_text(text):
    text = text.lower()
    return re.sub(r"[^\w\s]", "", text)


def load_all():
    with open("model/trained_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("model/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("model/label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    return model, vectorizer, label_encoder


def predict_label(text, model, vectorizer, label_encoder):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)
    return label_encoder.inverse_transform(pred)[0]
