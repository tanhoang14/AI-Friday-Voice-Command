import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

def speak(audio):
    print('F.R.I.D.A.Y.: ' + audio)
    friday.say(audio)
    friday.runAndWait()
speak("Hello Tan")
def time() :
    Time = datetime.datetime.now().strftime("%I : %M : %p")
    speak(Time)
def welcome() : 
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12 :
        speak("Good Morning Sir") 
    elif hour >= 12 and hour <= 18 :
        speak("Good Afternoon Sir") 
    elif hour >= 18 and hour <= 24 :
        speak("Good Night Sir") 
    speak('How can i help you')

    def command():
        c=sr.Recognizer()
        with sr.Mircrophone() as source:
            c.pause_threshold=2
            audio = c.listen(source)
        try: 
            query = c.recognize_google(audio, language='en')
            print("Tan :" + query)
        except sr.UnkownValueError:
            print("Please repeat or typing the command")
            query=str(input('Your order is: '))
            return query
    if __name__ =="__main__":
        weclome()
    while True:
        query= command().lower()
        if "google" in query: 
            speak("What should I search for?")
            search = command().lower()
            url=f"https://www.google.com/seach?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        elif "youtube" in query: 
            speak("What should I search for?")
            search = command().lower()
            url=f"https://www.youtube.com/seach?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open video":
            meme = r""
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Friday is out. Thank you and have a nice day Boss")
            quit()