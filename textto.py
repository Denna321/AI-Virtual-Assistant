import pyttsx3 


def texto(text):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate', 150) 
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()
