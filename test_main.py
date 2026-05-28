from fastapi.testclient import TestClient
from main import app

client = TestClient(app)   # creates a test client (no real server needed)


# ── Test 1: Root endpoint returns 200 OK
def test_root_returns_200():
    response = client.get("/")
    assert response.status_code == 200

# ── Test 2: Root endpoint returns expected message
def test_root_message():
    response = client.get("/")
    assert response.json() == {"message": "Sentiment API is running!"}

# ── Test 3: Predict returns 200
def test_predict_status():
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200

# ── Test 4: Positive text → positive sentiment
def test_predict_positive():
    response = client.post("/predict", json={"text": "This is awesome!"})
    assert response.json()["sentiment"] == "positive"

# ── Test 5: Negative text → negative sentiment
def test_predict_negative():
    response = client.post("/predict", json={"text": "This is terrible!"})
    assert response.json()["sentiment"] == "negative"

# ── Test 6: Response always contains 'sentiment' key
def test_predict_has_sentiment_key():
    response = client.post("/predict", json={"text": "hello world"})
    assert "sentiment" in response.json()