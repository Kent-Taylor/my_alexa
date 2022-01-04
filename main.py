# # pip install SpeechRecognition
# # pip install PyAudio -- you'll need this if you want to use Microphone as your source
# # pip install pywhatkit
# # pip install gtts
# # pip install playsound
#
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

        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        speech("How may I help you?") # changed from "say something"
        playsound("./sounds/activate.wav")
        sr.pause_threshold = 1
        sr.energy_threshold = 6
        audio = recorder.listen(source)

    speech_text = recorder.recognize_google(audio)
    print(f"You said: {speech_text}")
    return speech_text


text = get_audio()

if "youtube" in text.lower():
    speech("Okay, i will bring that up on youtube for you.")
    pywhatkit.playonyt(text)
elif "joke" in text.lower():
    speech("Knock knock, who's there? Boo. Boo who? Don't cry, i was just telling a joke")
elif "You are welcome" in text.lower():
    speech("Thank you for creating me Saltee_Killer")
else:
    pywhatkit.search(text)


# r = sr.Recognizer()
# keyword = "hello"
# with sr.Microphone() as source:
#     print("Speak:")
#     audio = r.listen(source)
#
# try:
#     if  r.recognize_google(audio) == keyword:
#         print("it worked")
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))