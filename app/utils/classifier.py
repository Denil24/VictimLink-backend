from transformers import pipeline

# ✅ Load pre-trained abuse classification model from Hugging Face
classifier = pipeline(
    "text-classification",
    model="unitary/toxic-bert",     # ✅ cloud-hosted
    tokenizer="unitary/toxic-bert"  # ✅ cloud-hosted
)

# Abuse categories (can be adjusted)
ABUSE_LABELS = ["Blackmail", "Harassment", "Scam", "Threat", "Hate Speech"]

def classify_text(text):
    results = []

    for label in ABUSE_LABELS:
        combined_text = f"{text} This message sounds like {label}."
        output = classifier(combined_text)[0]
        results.append((label, output['score']))

    best_label, best_score = max(results, key=lambda x: x[1])
    return best_label, round(best_score * 100, 2)
