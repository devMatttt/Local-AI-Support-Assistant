from fastapi import FastAPI
from app.logger import setup_logging
from app.config import Settings
from app.llm_client import ollama_client_request
from app.schemas import RequestModel, ResponseModel

import logging

app = FastAPI()
setup_logging()

@app.post("/chat-ai")
async def chat_request(request: RequestModel):
    response = ollama_client_request(request.prompt)

    return ResponseModel(response=response)