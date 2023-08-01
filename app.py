from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from datetime import datetime
import psutil

from middlewares.errorException import custom_exception_handler

from models.fileUpload import FileUploadRequestSchema, FileUploadResponseSchema
from models.speechToText import SpeechToTextRequestSchema, SpeechToTextResponseSchema
from models.textToSpeech import TextToSpeechRequestSchema, TextToSpeechResponseSchema

from services.cloudService import fileUploadService
from services.health import get_ram_available_mb
from services.soundAndText import audioToText, textToAudio

from utils.responseSchema import errorResponse, successResponse

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
   return custom_exception_handler(request, exc)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

deployedTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.get('/')
async def index():
   return successResponse("Welcome to FastAPI", {"deployedTime": deployedTime})

@app.post('/file-upload', response_model=FileUploadResponseSchema)
async def fileUpload(request: FileUploadRequestSchema):
    return {"url": fileUploadService(request.file)}
    
@app.post('/speech-to-text', response_model=SpeechToTextResponseSchema)
async def speechToTextFree(request: SpeechToTextRequestSchema):
    return successResponse("Success",{"text": audioToText(request.audio_url)})

@app.post('/text-to-speech', response_model=TextToSpeechResponseSchema)
async def textToSpeech(request: TextToSpeechRequestSchema):
    fileUrl = textToAudio(request.text)
    return successResponse("Success",{"url": fileUrl})

@app.get('/health')
def health_check():
    """Health check endpoint."""
    cpu_percent = psutil.cpu_percent()
    ram_available_mb = get_ram_available_mb()

    if app.state:
        return successResponse("Success",{
            "status": "UP",
            "cpu_percent": cpu_percent,
            "ram_available": ram_available_mb
        })
    else:
        return errorResponse("Error",{"status": "DOWN"})

