from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from pydantic import BaseModel
from decimal import Decimal, ROUND_HALF_UP

app = FastAPI()

class TextData(BaseModel):
    text: str

model = AutoModelForSequenceClassification.from_pretrained("cointegrated/rubert-tiny2-cedr-emotion-detection")
tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2-cedr-emotion-detection")

emotion_labels = ["грусть", "радость", "злость", "страх", "удивление"]

@app.post("/predict/")
def predict(text_data: TextData):
    text = text_data.text
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    emotion_probabilities = probabilities.tolist()[0]

    emotions = {}
    for i in range(len(emotion_labels)):
        emotion_probability = round(emotion_probabilities[i], 4)
        emotions[emotion_labels[i]] = emotion_probability

    response = {
        'текст': text,
        'эмоции': emotions
    }

    return response

@app.get("/")
def root():
    return {"message": "Hello World"}