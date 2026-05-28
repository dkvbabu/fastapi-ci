from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sentiment API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Sentiment API is running!"}

@app.post("/predict")
def predict(data: TextInput):
    # Simple rule-based sentiment (replace with real model)
    positive_words = ["love", "great", "awesome", "good", "excellent"]
    sentiment = "positive" if any(w in data.text.lower() for w in positive_words) else "negative"
    return {"text": data.text, "sentiment": sentiment}
