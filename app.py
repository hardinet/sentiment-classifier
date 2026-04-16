import gradio as gr
from transformers import pipeline

# On charge un modèle déjà entraîné par la communauté (plus simple pour débuter)
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    if not text:
        return "Veuillez entrer du texte."
    result = classifier(text)[0]
    label = result['label']
    score = round(result['score'], 4)
    # On traduit pour que ce soit plus sympa
    sentiment = "POSITIF 😊" if label == "POSITIVE" else "NÉGATIF 😡"
    return f"{sentiment} (Score de confiance : {score})"

# Création de l'interface
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(placeholder="Entrez un avis ou une news financière..."),
    outputs="text",
    title="Analyseur de Sentiments IA",
    description="Projet de classification de texte avec Hugging Face et Gradio.",
    examples=["The market is growing fast!", "This product is a total waste of money."]
)

if __name__ == "__main__":
    demo.launch()