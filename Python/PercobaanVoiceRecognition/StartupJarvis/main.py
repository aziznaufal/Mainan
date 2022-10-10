import os
from Python.PercobaanVoiceRecognition.PersonalAssistant.head import Head 

import time
from jazzit import waiting_track

@waiting_track("D:\MINE\Project\Personal\Mainan\Python\PercobaanVoiceRecognition\\asset\sound\mixkit-sci-fi-drone-hover-915.wav")

def run():
    jarvisHead = Head("en", 180)
    time.sleep(5)
    text = "Wellcome Sir!"
    jarvisHead.speak(text)
    time.sleep(0.5)
    text = " All System are ready to lunch!"
    jarvisHead.speak(text)
    time.sleep(2)


if __name__ == "__main__":
    run()