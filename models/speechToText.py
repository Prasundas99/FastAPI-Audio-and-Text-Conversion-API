from pydantic import BaseModel, Field


class SpeechToTextRequestSchema(BaseModel):
    audio_url: str 

class SpeechToTextResponseBody(BaseModel):
    text: str  

class SpeechToTextResponseSchema(BaseModel):
    success: bool
    message: str
    data: SpeechToTextResponseBody = None
