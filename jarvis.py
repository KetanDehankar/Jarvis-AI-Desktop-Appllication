# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:18:02 2021

@author: Keytan
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from pydub import AudioSegment
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am jarvis sir, Please tell me how may I help you")

def takeCommand():
    ## it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone(device_index= 1) as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said: {query}\n")
            
            
        except Exception as e:
            print("Say that again please..")
            return "None"
        
        return query
        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    
    
if __name__ == "__main__":
    speak("Ketan is a good boy")
    wishMe()
    while True:
      query = takeCommand().lower()
      
      
      if 'wikipedia' in query:
          speak('searching wikipedia...')
          query = query.replace("wikipedia", "")
          result = wikipedia.summary(query, sentences=2)
          speak("According to wikipedia")
          print(result)
          speak(result)
        
        
    query = takeCommand().lower()
    
    
elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
    
elif 'open google' in query:
        webbrowser.open("google.com")    
        
    
elif 'stackoverflow' in query:
        webbrowser.open("stackoverflow.com")        
        
elif 'play music' in query:        
     music_dir = "C:\\Users\\Keytan\\Desktop\\Railway"
     songs = os.listdir( music_dir )
     print(songs)
     os.startfile(os.path.join(music_dir, songs[0]))
     
elif 'the time' in query:
    strTime = datetime.datatime.now().strftime("%H:%M:%S")
    speak(f" thetime is {strTime}")
    
    
elif 'open code' in query:
   CodePath = " D://MCA//iwt lab1//Microsoft VS Code//Code.exe"
   os.startfile(CodePath)
   
elif 'email to ketan' in query:
    try:
        speak("what should i say?")
        content = takeCommand()
        to = "anyemailaddress@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry my friend ketan bhai. i am not able to send this email")
        