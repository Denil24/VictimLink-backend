from transformers import pipeline

# Load model and tokenizer from local path
classifier = pipeline(
    "text-classification",
    model="app/models/toxic_bert",
    tokenizer="app/models/toxic_bert"
)

# Abuse categories (you can tweak or expand this list)
ABUSE_LABELS = ["Blackmail", "Harassment", "Scam", "Threat", "Hate Speech"]

# Dummy mapping logic for now (based on max score)
def classify_text(text):
    results = []

    for label in ABUSE_LABELS:
        # Construct prompt-like input (helps with classification signal)
        combined_text = f"{text} This message sounds like {label}."
        output = classifier(combined_text)[0]
        results.append((label, output['score']))

    best_label, best_score = max(results, key=lambda x: x[1])
    return best_label, round(best_score * 100, 2)
