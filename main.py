# pip install SpeechRecognition
# pip install PyAudio -- you'll need this if you want to use Microphone as your source
# pip install pywhatkit
# pip install gtts
# pip install playsound

import speech_recognition as sr
import pywhatkit
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")


def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        speech("Say something")
        playsound("./sounds/activate.wav")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"You said: {text}")
    return text


text = get_audio()

if "youtube" in text.lower():
    speech("Okay, i will bring that up on youtube for you.")
    pywhatkit.playonyt(text)
elif "joke" in text.lower():
    speech("Knock knock, who's there? Boo. Boo who? Don't cry, i was just telling a joke")
else:
    pywhatkit.search(text)