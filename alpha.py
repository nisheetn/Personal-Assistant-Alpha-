# To use this assiatant please do pip install pyttsx3
#  To use this assiatant please do pip install speechRecognition
# To use this please do pip install google,wikipedia and os  
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia 
import googlesearch 
import os 
import random
import smtplib 
import webbrowser 
#microsoft speech api 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait() 

def wish():
    currenthour=int(datetime.datetime.now().hour)
    if currenthour in range (0,13):
        speak("I wish you a very good morning")
    elif currenthour in range (13,18):
        speak ("I wish you a very good afternoon")
    else :
        speak("I wish you a very good evening")
    speak ("My name is alpha, how can I assist you today Nisheet?") 

def voiceassist():
    # speech Recognization 
    # It takes input through the microphone and produces output as String
  
    r=sr.Recognizer() 
    with sr.Microphone() as source :
        print ("Listening......") 
        r.pause_threshold = 1
        audio=r.listen(source)
    try :
        print("Recongizing..")
        x=r.recognize_google(audio,language='en-ca')
        print (f"User said :{x}\n")
    except Exception as e :
        print("How can I help?")
        return "None" 

    return x

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail_here','yourpassword')
    server.sendmail('youremail_here',to,content)
    server.close()

if __name__=="__main__" :
    wish()
    while True:

        x=voiceassist().lower()

        if 'wikipedia' in x:
            speak('Searching Wikipedia, Please wait ......')
            x=x.replace("Wikipedia","")
            results=wikipedia.summary(x,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results) 
        elif 'open youtube' in x:
            webbrowser.open("youtube.com")
        elif 'open google' in x :
            webbrowser.open("google.com")
        elif "play music" in x:
            webbrowser.open("https://www.youtube.com/watch?v=_pLO4jFDeIc")

        elif "open vs code" in x :
            location_for_vscode="C:\\Users\\nishe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(location_for_vscode)
        elif 'email to john' in x :
            try:
                speak("What to write")
                content=voiceassist()
                to="receivers_email"
                speak("EMAIL SENT")
            except Exception as e :
                print(e)
                speak('Email cant be sent ')
        elif 'search google' in x :
            speak("What to search?")
            content=voiceassist()
            speak("Searching") 
            try: 
                from googlesearch import search 
            except ImportError:  
                print("No module named 'google' found") 
  
            for j in search(content, tld="co.in", num=10, stop=10, pause=2): 
                print(j)
        elif 'search youtube' in x:
            speak("What to search?")
            content=voiceassist()
            speak("Searching")
        elif 'the time' in x :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}") 
        elif 'birthday' in x :
            speak ("December")
        elif "stop" in x:
            break 



























 


