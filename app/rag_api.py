import heapq

try:
    from config import label_knowledge
except:
    from .config import label_knowledge
import heapq

from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()


model = SentenceTransformer("all-mpnet-base-v2")
label_embeddings = {
    label: model.encode(desc) for label, desc in label_knowledge.items()
}


class RequestText(BaseModel):
    text: str
    top_k: int = 3


@app.post("/rag-predict")
def predict(request: RequestText):
    clean_text = request.text.strip().replace("\n", " ").replace("\r", " ")

    text_emb = model.encode(clean_text)
    sims = {
        label: cosine_similarity([text_emb], [emb])[0][0]
        for label, emb in label_embeddings.items()
    }
    top_labels = heapq.nlargest(request.top_k, sims.items(), key=lambda x: x[1])
    return {"labels": [label for label, score in top_labels]}
