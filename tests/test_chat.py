from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_normal_chat_request():
    response = client.post("/chat-ai", json={"prompt": "Hello, how are you?"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_empty_prompt():
    response = client.post("/chat-ai", json={"prompt": ""})
    assert response.status_code == 422

def test_long_prompt():
    long_prompt = "a" * 2001
    response = client.post("/chat-ai", json={"prompt": long_prompt})
    assert response.status_code == 422

def test_down_ollama_client(monkeypatch):
    monkeypatch.setenv("MODEL_HOST", "http://0.0.0.0:11434")

    response = client.post("/chat-ai", json={"prompt": "Hello, how are you?"})
    assert response.status_code == 504