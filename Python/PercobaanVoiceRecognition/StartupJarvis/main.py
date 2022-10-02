import os
from Python.PercobaanVoiceRecognition.PersonalAssistant.head import Head 
import winsound

jarvisHead = Head("en", 180)

text = "Wellcome Sir! All System are ready to lunch!"
jarvisHead.speak(text)

