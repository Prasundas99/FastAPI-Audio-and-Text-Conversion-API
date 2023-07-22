import assemblyai as aai
from gtts import gTTS

from services.cloudService import fileUploadService


def audioToText(audioUrl):
    aai.settings.api_key = "21008ed8ba434b078f262fec17016cd1"
    transcriber = aai.Transcriber()
    try:
        print("Transcribing...")
        transcript = transcriber.transcribe(audioUrl)
        print("Transcription complete!")
        print(transcript.text)
        return transcript.text
    
    except aai.ApiException as e:
        print(e, "Transcription failed.")
        return "Transcription failed."
    

def textToAudio(inputText):
    print(inputText)
    language = 'en'
    myobj = gTTS(text=inputText, lang=language, slow=False)
    myobj.save("welcome.mp3")
    file = open("welcome.mp3", "rb")
    print(file)
    uploadedFile = fileUploadService(file)
    print(uploadedFile)
    file.close()
    return uploadedFile