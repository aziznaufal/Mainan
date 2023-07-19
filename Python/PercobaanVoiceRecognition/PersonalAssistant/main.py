import head as h
import pronunciation as pron

myhead = h.Head("en", 180)

def run():
    myhead.listen()
    # myhead.speak("Welcome Sir")
    # myhead.speak("Hello Sir")

if __name__ == "__main__":
    # run()
    # Pron = pron.TextToSpeech()
    # x = Pron.getList()
    # for item in x:
    #     print(item)
    # print('Done')
    list = {'AH','B','IY','S','D','EH','F','JH','EY','CH','AY','K','L','M','N','OW','P','Y','UW','AA','R','T','V','W','Z'}
    list2 = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z'}
    # for item in list:
    #     print(item)
    #     myhead.speak(item)
    for item in list2:
        print(item)
        myhead.speak(item)
    print('Done.!!!')