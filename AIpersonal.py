#functionality
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
import pyaudio

#voice
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Tells me the time
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

#How command taking works
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Mark is getting ready, please wait one moment.")
speak("Mark is getting ready, please wait one moment.")
wishMe()
time.sleep(3)

if __name__=='__main__':


    while True:
        speak("Hello Sir, my name is Mark, your artificial intelligence assistant. How may I help you today?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Have a good day sirr")
            print("Have a good day sir")
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2000)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        elif 'open protonmail' in statement:
            webbrowser.open_new_tab("inbox.protonmail.com")
            speak("Protonmail is now open sir")
            time.sleep(5)
        elif 'open discord' in statement:
            webbrowser.open_new_tab("https://discord.com/channels/@me")
            speak("Discord is now open sir")
            time.sleep(5)
        elif 'open the NewYork Times' in statement:
            webbrowser.open_new_tab("https://www.nytimes.com/")
            speak("Enjoy reading the NewYork Times sir")
            time.sleep(5)
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.wsj.com/")
            speak('Here are some headlines from the The Wall Street Journal, Happy reading')
            time.sleep(5)
        elif 'open spotify' in statement:
            spotify = webbrowser.open_new_tab("open.spotify.com")
            speak("Enjoy your music sir.")
            time.sleep(5)
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)	
     
# Tells me the time     
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is {strTime}")
# AI Identity     
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Mark your personal assistant. I am programmed to minor tasks like'
                  'open youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was open source code remade by my master")
            print("I was open source code remade by my master")
#Signs out of computer
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
