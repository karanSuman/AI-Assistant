import psutil
import pyttsx3  # pip install pyttsx3 (Basically pyttsx3 is a module)
import datetime  # importing datetime module
import speech_recognition as sr  # pip install speechRecognition (Speech Recognition is a module)
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os 
import pyautogui
import pyjokes   # pip install pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Use [0] for Male voice & [1]  for female Voice
engine.setProperty('voice', voices[0].id)
newVoiceRate = 150  # Slowing down the speed of the voice
engine.setProperty('rate', newVoiceRate)


def speak(audio):  # Creating a function
    engine.say(audio)
    engine.runAndWait()  # playing the voice


def time():
    # strftime extracts the actual date from now function(in string format)
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current Time is")
    speak(Time)


def date():
    # year extracts the actual year from now funtion(in integer format)
    year = int(datetime.datetime.now().year)
    # month extracts the actual month from now funtion(in integer format)
    month = int(datetime.datetime.now().month)
    # date extracts the  actual date from now function(in integer format)
    date = int(datetime.datetime.now().day) 
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme(): # Calling All the Previous Functions
    speak("Welcome Back Sir! ")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
           speak("Good morning")
    elif hour >=12 and hour <18:
           speak("Good afternoon")
    elif hour >=18 and hour <=24:
           speak("Good evening")
    else:
        speak("Good Night")
    speak("Lucifer at your service. How I can help you?")
   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language= "en=in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please..")
 
        return"None"

    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login("Test@gnail.com", "Password") #Enter your gmail and Password
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU ids at " + usage)

    battery= psutil.sensors_battery
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())
   
if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
             speak("Searching....")
             query = query.replace("wikipedia", "")
             result = wikipedia.summary(query,sentences = 2)
             speak(result)
        elif "send email" in query:
             try:
                 speak("What should I Say ?")
                 content=takeCommand()
                 to ="Xyz@gmail.com" #Destination Email
                 #sendmail(to, content)
                 speak(content)
             except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
             speak("What should I search?")
             chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
             search = takeCommand().lower()
             wb.get(chromepath).open(search+ ".com")

        elif "logout" in query:
              os.system("shutdown /s /t 1")

        elif "shutdown " in query:
              os.system("shutdown - 1")
        
        elif "restart" in query:
              os.system("shutdown /r /t 1")
         
        elif " play songs" in query:
            songs_dir="F:\kk"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        
        elif "remember that" in query:
            speak("What should i Remember ?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember= open("data.txt", "w")
            remember.write(data)
            remember.close() 

        elif "do you know anything" in query:
             remember = open("data.txt", "r")
             speak("you said to me remember that" + remember.read())

        elif "screenshot" in query:
              screenshot()
              speak("Done...!")

        elif  "cpu" in query:
             cpu()

        elif "joke" in query:
            jokes()
         