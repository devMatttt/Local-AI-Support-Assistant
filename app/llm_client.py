from ollama import Client
from app.config import Settings
from fastapi import HTTPException

import logging

logger = logging.getLogger(__name__)

def ollama_client_request(prompt: str):

    if not prompt:
        logging.warning("Received empty prompt for ollama_client_request.")


    try:
        
        settings = Settings()

        logging.info(f"Using model: {settings.model}")
        logging.info(f"Client host: {settings.model_host}")

        client = Client(host=settings.model_host)

        response = client.chat(
            model=settings.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content
    except Exception as e:
        logging.error(f"Error in ollama_client_request: {e}")

        raise HTTPException(
            status_code=504,
            detail=f"Ollama server is down or unreachable."
        )