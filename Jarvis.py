import datetime 
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib
import pyautogui
import psutil
import pyjokes
import pyttsx3
import sys
from sys import platform
#from youtube import youtube
import getpass

engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
newvoicerate=190
engine.setProperty('rate', newvoicerate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Hello  This is JARVIS")

def time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time  is")
    speak(time)

def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\AI assiatant\ss.jpg")

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("Todays date is")
    speak(day)
    speak(month)
    speak(year)   

def wishme():
    speak("Welcome back ")

    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good morining sir")
    elif hour>12 and hour<=18:
        speak("Good afternoon sir")
    elif hour>18 and hour<=24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Jarvis at your service, how can i help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)
    try:
        print("Recognising...")
        query= r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please..")
        return "None"
    return query

if __name__== "__main__":
    wishme()
    platform == "win32"
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    while True:
        query=takeCommand().lower()
        print(query)
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab("https://stackoverflow.com")

        elif 'offline' in query:
            quit()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'send email' in query:
            try:
                speak("what should i say? ")
                content=takeCommand()
                to="xyz@gamil.com"
                sendEmail(to,content)
                speak(content)
            except Exception as e:
                speak(e)
                speak("Unable to send email")

        elif "search in chrome" in query:
            speak("What should i search")
            gpath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search=takeCommand().lower()
            webbrowser.get(gpath).open_new_tab(search+" .com")

        elif "logout" in query:
            os.system("shutdown -1")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            ath="Music"
            song=os.listdir(ath)
            os.startfile(os.path.join(ath,song[0]))

        elif "remember" in query:
            speak("what should i remember")
            data=takeCommand()
            speak("You said to me remember"+data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember.open("data.txt","r")
            speak("you said to me to remember"+remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("your screen shot is saved!")

       # elif "cpu" in query():
        #    cpu()
         #   speak("your task is done!")
        elif "joke" in query:
            joke()

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)

        elif "gaana" in query:
            webbrowser.get('chrome').open_new_tab("gaana.com")
            
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'your master' in query:
            if platform == "win32":
                speak('Nikhil is my master. she created me couple of days ago')

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())



