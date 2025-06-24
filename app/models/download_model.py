from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Download and save model to local folder
model_name = "facebook/bart-large-mnli"

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./app/models/bart")
tokenizer.save_pretrained("./app/models/bart")
