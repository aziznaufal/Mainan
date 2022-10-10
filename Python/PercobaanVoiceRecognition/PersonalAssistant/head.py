import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
from playsound import playsound
import os
import pyttsx3


class Head:

    def __init__(self, lang, speakRate=300):
        self.language = lang
        self._speakEngine = pyttsx3.init()
        voices = self._speakEngine.getProperty("voices")
        self._speakEngine.setProperty("rate", speakRate) 
        self._speakEngine.setProperty("voice", voices[1].id)

    def speak(self, text):
        # mp3_fp = BytesIO()
        # tts = gTTS(text, lang = self.language, tld='co.uk')
        # tts.write_to_fp(self.tempMp3File)
        # playsound(self.tempMp3File)
        # os.remove(self.tempMp3File)
        self._speakEngine.say(text)
        self._speakEngine.runAndWait()

    def listen(self):
        self.speak("I'm Listening")
        recording = sr.Recognizer()
        with sr.Microphone() as source: 
            recording.adjust_for_ambient_noise(source)
            audio = recording.listen(source)

        try:
            word = recording.recognize_google(audio)
            self.speak("You Said: " + word)
        except Exception as e:
            self.speak("I'm Sorry Sir, I Can't Hear You")