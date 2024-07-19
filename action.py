import textto
import spt
import datetime
import webbrowser
def Action(data):
    user_data=data.lower()

    if "what is your name" in user_data:
        textto.texto("my name is laura your virtual friend")
        return "my name is laura your virtual friend"
    elif "hello" in user_data or "hi" in user_data:
        textto.texto("hello how can i help u ")
        return "hello how can i help u "
    elif "good morning" in user_data:
        textto.texto("good day friend!")
        return "good day friend!"
    elif "what is the time now" in user_data:
        curt=datetime.datetime.now()
        Time = (str)(curt.hour)+ " Hour : ", (str)(curt.minute) + " Minute"
        textto.texto(Time)
        return Time
    elif "shutdown" in user_data:
        textto.texto("ok sir")
        return "ok sir"
    elif 'open google' in user_data or 'google'  in user_data:
            url = 'https://google.com/'
            webbrowser.open(url)
            textto.texto("google open") 
            return "google open"
            
    elif 'open youtube' in user_data or 'youtube'  in user_data:
            url = 'https://youtube.com/'
            webbrowser.open(url)
            textto.texto("youtube open")
            return "youtube open" 
    else:
        textto.texto("sorry i cannot understand please try again")
        return "sorry i cannot understand please try again"