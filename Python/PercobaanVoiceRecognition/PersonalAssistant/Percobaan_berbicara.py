# from gtts import gTTS
# from io import BytesIO
# from playsound import playsound

# language = 'en'
# text = "Welcome back Sir"
# file_name = "hello_bonjour.mp3"

# tts_en = gTTS('hello', lang='en')
# tts_fr = gTTS('bonjour', lang='fr')

# with open(file_name, 'wb') as f:
#     tts_en.write_to_fp(f)
#     tts_fr.write_to_fp(f)

# playsound(file_name)

import pyttsx3

# _speakEngine = pyttsx3.init()
# _speakEngine.setProperty("rate", 200) 
# text = "Welcome back Sir"

# _speakEngine.say(text)
# _speakEngine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# for voice in voices:
engine.setProperty('voice', voices[1].id)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()