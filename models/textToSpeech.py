from pydantic import BaseModel, Field


class TextToSpeechRequestSchema(BaseModel):
    text: str

class TextToSpeechResponseBody(BaseModel):
    url: str = Field(...)

class TextToSpeechResponseSchema(BaseModel):
    success: bool
    message: str
    data: TextToSpeechResponseBody = None
