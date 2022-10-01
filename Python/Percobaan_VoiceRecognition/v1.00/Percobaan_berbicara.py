from gtts import gTTS
from io import BytesIO
from playsound import playsound

language = 'en'
text = "Welcome back Sir"
file_name = "hello_bonjour.mp3"

tts_en = gTTS('hello', lang='en')
tts_fr = gTTS('bonjour', lang='fr')

with open(file_name, 'wb') as f:
    tts_en.write_to_fp(f)
    tts_fr.write_to_fp(f)

playsound(file_name)