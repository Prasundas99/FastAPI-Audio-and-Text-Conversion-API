import assemblyai as aai
from gtts import gTTS
from cloud import fileUpload

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
    # Language in which you want to convert
    language = 'en'
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=inputText, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")
    
    ## extract the saved mp3 file to save it in the database
    file = open("welcome.mp3", "rb")
    uploadedFile = fileUpload(file)
    print(uploadedFile)
    file.close()
    return file