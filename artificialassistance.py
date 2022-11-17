import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audiovoice):
    #engine.say('hello dear')
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()


def greet():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<=11:
        speak('good morning sir')
    elif hour>=11 and hour<15:
        speak('good afternoon sir')
    elif hour>=15 and hour<=24:
        speak('good night sir')
    speak('i am your personal assistance')

def askname():
    speak('what is your name sir')
    name=takevoicecommand()
    speak('welcome '+name)
    speak('how can i help you sir?')

text=''
def takevoicecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold=1
        try:
            audio=r.listen(source,timeout=30,phrase_time_limit=10)
            print('compiling your voice please wait...')
            text=r.recognize_google(audio,language='en-in')
            print(text)
        except Exception as e:
            speak('unable to recognize your voice')
        return text

#speak('my audio voice')

if __name__=='__main__':
    greet()
    askname()
    while True:
        work=takevoicecommand().lower()
        if 'how are you' in work:
            speak('i am fine. thank you')
            speak('how are you sir?')
        elif 'fine' in work or 'good' in work:
            speak('i am glad to know you that you are fine')
        elif 'i love you' in work or 'love you' in work:
            speak('oh my god  thank you')
        elif 'open notepad' in work:
            path='c:\\windows\\system32\\notepad.exe'
            os.startfile(path)
        elif 'close notepad' in work:
            os.system('TASKKILL/F /IM notepad.exe')
        elif 'open chrome' in work:
            url='techsrijan.com'
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        elif 'close chrome' in work:
            os.system('TASKKILL/F /IM chrome.exe')
        elif 'bye' in work:
            speak('bye sir... see you again')
            exit()
        else:
            speak('i can not understand please speak again')

