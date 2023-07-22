from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from datetime import datetime

from models.fileUpload import FileUploadRequestSchema, FileUploadResponseSchema
from models.speechToText import SpeechToTextRequestSchema, SpeechToTextResponseSchema
from models.textToSpeech import TextToSpeechRequestSchema, TextToSpeechResponseSchema
from services.cloudService import fileUploadService
from services.soundAndText import audioToText, textToAudio

from utils.responseSchema import successResponse, errorResponse

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(exc.detail, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(exc, status_code=status.HTTP_400_BAD_REQUEST)


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
    successResponse("Welcome to FastAPI", {"deployedTime": deployedTime})

@app.post('/file-upload', response_model=FileUploadResponseSchema)
async def fileUpload(request: FileUploadRequestSchema):
    return {"url": fileUploadService(request.file)}
    
@app.post('/speech-to-text', response_model=SpeechToTextResponseSchema)
async def speechToText(request: SpeechToTextRequestSchema):
    return successResponse("Success",{"text": audioToText(request.audio_url)})

@app.post('/text-to-speech', response_model=TextToSpeechResponseSchema)
async def textToSpeech(request: TextToSpeechRequestSchema):
    fileUrl = textToAudio(request.text)
    return successResponse("Success",{"url": fileUrl})


