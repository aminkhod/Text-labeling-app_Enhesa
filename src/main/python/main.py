import os
import re

import gradio as gr
import joblib
import pandas as pd
import plotly.express as px
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
    VotingClassifier,
)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC

app = FastAPI()
# lodad joblib
vectorizer = joblib.load("../models/vectorizer.pkl")
model = joblib.load("../models/ensemble_model.pkl")


class InputText(BaseModel):
    text: str


@app.post("/predict")
def get_prediction(input: InputText):
    cleaned = clean_text(input.text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)
    label = le.inverse_transform(pred)[0]
    return {"prediction": label}
