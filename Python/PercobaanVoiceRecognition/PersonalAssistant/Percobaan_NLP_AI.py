import os
import speech_recognition as sr
import pyttsx3
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download("punkt")
# nltk.download("wordnet")
# nltk.download("stopwords")

def personal_assistant():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hi, I'm your personal assistant! How can I help you today?")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
            
            # NLP processing
            words = word_tokenize(text)
            words = [word.lower() for word in words if word.isalpha()]
            stop_words = set(stopwords.words("english"))
            words = [word for word in words if not word in stop_words]
            lemmatizer = WordNetLemmatizer()
            words = [lemmatizer.lemmatize(word) for word in words]
            
            # Machine learning and AI
            # Here, you would need to train a model to recognize patterns in the user's input
            # and respond in a way that aligns with the persona of the personal assistant
            # This is a complex task that requires a good understanding of machine learning
            # and NLP, as well as access to large amounts of training data
            
            engine = pyttsx3.init()
            engine.say("You said: {}".format(text))
            engine.runAndWait()
        except:
            print("Sorry, I could not recognize what you said.")

personal_assistant()