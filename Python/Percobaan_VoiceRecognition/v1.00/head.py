import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
from playsound import playsound
import os

class Head:
    def __init__(self, lang):
        self.language = lang

    def speak(self, text):
        file_name = "file_1.mp3"
        mp3_fp = BytesIO()
        tts = gTTS(text, lang = self.language, tld='co.uk')
        tts.save(file_name)
        playsound(file_name)
        os.remove(file_name)

    def listen(self):
        self.speak("Welcome Sir, please say something")
        recording = sr.Recognizer()
        with sr.Microphone() as source: 
            recording.adjust_for_ambient_noise(source)
            audio = recording.listen(source)

        try:
            word = recording.recognize_google(audio)
            self.speak("You Said: " + word)
        except Exception as e:
            self.speak("I'm Sorry Sir, I Can't Hear You")