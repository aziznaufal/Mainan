import speech_recognition as sr
from gtts import gTTS



recording = sr.Recognizer()

print("Please Say something:")
with sr.Microphone() as source: 
    recording.adjust_for_ambient_noise(source)
    audio = recording.listen(source)

try:
   print("You said: \n" + recording.recognize_google(audio))
except Exception as e:
   print(e)

