from turtle import title

from pydantic import BaseModel, Field

class RequestModel(BaseModel):
    prompt: str = Field(
        title="Prompt",
        description="The input prompt for the language model",
        min_length=1,
        max_length=2000,
    )

class ResponseModel(BaseModel):
    response: str