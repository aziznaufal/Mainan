import os
from Python.PercobaanVoiceRecognition.PersonalAssistant.head import Head 

import time
from jazzit import waiting_track

# @waiting_track("D:\MINE\Project\Personal\Mainan\Python\PercobaanVoiceRecognition\\asset\sound\mixkit-dark-synth-oscillator-646.wav")

def run():
    jarvisHead = Head("en", 180)
    time.sleep(2)
    text = "Wellcome Sir!"
    jarvisHead.speak(text)
    time.sleep(0.25)
    text = " All System are ready to lunch!"
    jarvisHead.speak(text)
    time.sleep(1.25)


if __name__ == "__main__":
    run()