# # pip install SpeechRecognition
# # pip install PyAudio -- you'll need this if you want to use Microphone as your source
# # pip install pywhatkit
# # pip install gtts
# # pip install playsound
#
import random
import speech_recognition as sr
import pywhatkit
from gtts import gTTS
from playsound import playsound



# try:
#     said = sr.recognize_google(audio)
#     print(f"You said: {said}")
# except Exception as e:
#     print(f"I think you are at very noisy place,\nThis is the error in computer languge: {str(e)}")

r2_sounds = ["./sounds/Beeping_and_whistling.mp3", "./sounds/R2_taking_the_comlink.mp3", "./sounds/R2_taking_to_himself.mp3"]


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    playsound(random.choice(r2_sounds))
    output.save("./sounds/output.mp3")
    # playsound("./sounds/output.mp3")


def get_audio():
    while True:
        recorder = sr.Recognizer()
        with sr.Microphone() as source:

            # sr.pause_threshold = 1
            # sr.energy_threshold = 6
            audio = recorder.listen(source)


        speech_text = recorder.recognize_google(audio)
        print(speech_text)

        if "R2-D2" in speech_text:
            speech("\tHow may I help you?") # changed from "say something"
            playsound("./sounds/activate.wav")
        else:
            break

    return speech_text


text = get_audio()

playsound(random.choice(r2_sounds))
if "youtube" in text.lower():
    speech("\tOkay, i will bring that up on youtube for you.")
    pywhatkit.playonyt(text)
elif "joke" in text.lower():
    speech("\tKnock knock, who's there? Boo. Boo who? Don't cry, i was just telling a joke")
elif "You are welcome" in text.lower():
    speech("\tThank you for creating me Saltee_Killer")
else:
    pywhatkit.search(text)

# Download the R2-D2 sounds here: https://www.soundboard.com/sb/r2d2_r2_d2_sounds