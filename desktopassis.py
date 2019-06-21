import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia#pip install wikipedia
from playsound import playsound
import random
import pyautogui as py
import webbrowser
import requests
import os
import smtplib
import time
#-----------------intilization---------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#----------------wishing-------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    time.sleep(0.30)
    speak("I am HAZEL . Please tell     me    how    may    I    help   you")       
#--------------------------------------------------
#------------take orders---------------------------
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
#--------------------------------------------------------------
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
#---------------------------------------------------------------
#-------------------LOOP--------------------------------------
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'search youtube' in query:
            webbrowser.open("youtube.com")
        elif 'search ' in query:
            query = query.replace("search", "")
            speak(f"here is something i found on internet for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif 'joke' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
        elif "show me videos of" in query:
            query=query.replace("show me videos of","")
            speak(f"showing videos for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}.com")
        elif 'search google' in query:
            webbrowser.open("google.com")
        elif 'search stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "tell me about yourself" in query:
            speak("hello i am assistant created by mr. prakhar dubey")
        elif "maximize this window" in query:
            py.hotkey("win","up")
        elif "minimise this window" in query:
            py.hotkey("win","down")
        elif "close this window" in query:
            py.hotkey("alt","f4")
        elif 'press' in query:
            dad=query.replace('press',"")
            print(dad)
            py.press(dad)
        elif "who is" in query:
            query=query.replace("who is","")
            speak(query+" is")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif"what is" in query :
            speak("OK")
            query=query.replace("what is","")
            speak(f"{query} is")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "where is" in query:
            query=query.replace("where is","")
            speak(f"{query} is in")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend bhai. I am not able to send this email")
        elif "show me pictures of" in query:
            query = query.replace("show me pictures of", "")
            speak(f"showing pictures of{query}")
            webbrowser.open(f"https://www.google.com/search?q={query}&rlz=1C1CHBF_enIN844IN844&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjqt7HcgLTiAhUFeisKHU_dD8AQ_AUIDigB&biw=820&bih=369")
        elif "take a screenshot" in query:
            speak("ok")
            query=query.replace("take a screenshot","")
            d=random.randint(39699966,69696699)
            py.screenshot(f"shot{d}.jpeg")
            playsound("sound3.mp3")
