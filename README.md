# Local AI Support Assistant — Phase 1 Final Assessment

A robust, privacy-first local AI support backend service built with **FastAPI**, **Pydantic**, and **Ollama**, featuring strict input validation and automated integration testing via **Pytest**.

---

## 🛠️ Setup

1. Download and install python. [text](https://www.python.org/).

2. Download and install ollama. [text](https://ollama.com/download/windows).

3. Run ollama --version to verify the successful installation then run "ollama pull qwen2.5-coder:7b" or choose the suitable model based on your GPU VRAM.

4. Fork or Clone https://github.com/devMatttt/Local-AI-Support-Assistant in your local device.

---
## How to Run?

1. Run "python -m venv venv" and activate it using bash "source venv/Scripts/activate"

2. Run "pip install -r requirements.txt" to install the required libraries.

3. Run "uvicorn app.main:app --reload" to run the uvicorn server.

4. Go to http://127.0.0.1/docs to test the chatbot AI api.

Enjoy!

---
## 📁 Project Structure

```text
phase1-final-assessment/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point & routing
│   ├── llm_client.py    # Ollama integration and client communication layer
│   └── schemas.py       # Pydantic request & response validation models
├── tests/
│   ├── __init__.py
│   └── test_chat.py     # Endpoint unit and integration tests
├── .env                 # Local environment configurations
├── .env.example         # Template environment variables file
├── requirements.txt     # Python project dependencies
└── README.md            # Project documentation