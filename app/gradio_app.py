import gradio as gr

from model import load_all, predict_label

model, vectorizer, label_encoder = load_all()


def classify(text):
    return predict_label(text, model, vectorizer, label_encoder)


demo = gr.Interface(
    fn=classify, inputs="textbox", outputs="label", title="Text Classifier"
)

demo.launch(server_name="0.0.0.0", server_port=7860)
