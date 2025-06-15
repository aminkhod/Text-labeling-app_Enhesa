import heapq

import gradio as gr

try:
    from config import label_knowledge
except:
    from .config import label_knowledge
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Embedder
model = SentenceTransformer("all-mpnet-base-v2")
label_embeddings = {
    label: model.encode(desc) for label, desc in label_knowledge.items()
}


def rag_predict(text, top_k=3):
    text_emb = model.encode(text)
    sims = {
        label: cosine_similarity([text_emb], [emb])[0][0]
        for label, emb in label_embeddings.items()
    }
    top_labels = heapq.nlargest(top_k, sims.items(), key=lambda x: x[1])
    return ", ".join([label for label, score in top_labels])


gr.Interface(
    fn=rag_predict,
    inputs="textbox",
    outputs="textbox",
    title="Multi-label Text Classifier (RAG)",
    description="RAG-style classifier using all-mpnet-base-v2 embeddings.",
).launch(server_name="0.0.0.0", server_port=7861, share=True)
