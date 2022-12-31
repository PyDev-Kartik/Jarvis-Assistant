import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import time
Assistant=pyttsx3.init('sapi5')
voices=Assistant.getProperty("voices")
Assistant.setProperty("voices",voices[0].id)

def Speak(Audio):
    Assistant.say(Audio)
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        command.pause_threshold =1
        audio=command.listen(source)

        try:
            print("Recognizing.....")
            query=command.recognize_google(audio,language="en-in")
            print(f"You Said : {query}")
        except Exception as Error:
            return "none"

        return query.lower()
def TaskExe():

    def Music():
        Speak("Tell The name of the song")
        musicName=takecommand()
        search=musicName.lower()
        pywhatkit.playonyt(search)
        Speak("Your song has been started, enjoy sir")
    def Movie():
        Speak("Tell me the name of movie")
        movieName=takecommand()
        search=movieName.lower()
        pywhatkit.playonyt(search+" full movie in hindi")
        Speak("Your movie has been started, enjoy sir")  
    def Trailer():
        Speak("Tell me the name of movie")
        movietrailerName=takecommand()
        search=movietrailerName.lower()
        pywhatkit.playonyt(search+" trailer in hindi")
        Speak("Your trailer has been started, enjoy sir")
    def Whatsapp():
        Speak("Tell me the name of person")
        name=takecommand()
        if 'kartik' in name:
            Speak("Tell me the message")
            msg=takecommand()
            Speak("Tell me the time sir")
            Speak("Time in hour ")
            hour=int(takecommand())
            Speak("Time in minutes ")
            minu=int(takecommand())
            pywhatkit.sendwhatmsg("+918758926708",msg,hour,minu,20)
            Speak("Ok sir, sending whatsapp message")
        elif 'aakruti'or'aakriti' in name:
            Speak("Tell me the message")
            msg=takecommand()
            Speak("Tell me the time sir")
            Speak("Time in hour ")
            hour=int(takecommand())
            Speak("Time in minutes ")
            min=int(takecommand())
            pywhatkit.sendwhatmsg("+917984299346",msg,hour,min,20)
            Speak("Ok sir, sending whatsapp message")
        else:
            print("error")
    while True:
        Speak("What can i do for you sir ? ")
        query=takecommand()
        time.sleep(4)

        if 'hello' in query.lower():
            Speak("Hello Sir")
        elif 'bye' in query.lower():
            Speak("ok bye sir have a good day ")
            break
        elif 'nothing' in query.lower():
            Speak("Ok Sir")
            break
        elif 'youtube search' in query.lower():
            Speak("Ok Sir this what i have found for you")
            query=query.lower().replace("jarvis","")
            query=query.lower().replace("youtube search","")
            web="www.youtube.com/results?search_query="+ query
            webbrowser.open(web)
            Speak("Done Sir")
        elif 'google search' in query.lower():
            Speak("Ok Sir this what i have found for you")
            query=query.lower().replace("jarvis","")
            query=query.lower().replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir")
        elif 'website' in query.lower():
            Speak("Ok Sir, launching")
            query=query.lower().replace("jarvis","")
            query=query.lower().replace("website","")
            query=query.lower().replace("open","")
            search=str(query)
            web2='https://www.'+search+ '.com'
            webbrowser.open(web2)
            Speak("Launched sir")     
        elif 'music' in query.lower():
            Music()
        elif 'wikipedia' in query.lower():
            Speak("Searching wikipedia")
            query=query.lower().replace("jarvis","")
            query=query.lower().replace("wikipedia","")
            data=wikipedia.summary(query,3)
            try:
                Speak(f"According to wikipedia :{data}")
                break
            except Exception as error:
                return "none"
                continue
        elif 'whatsapp' in query.lower():
            Whatsapp()
        elif 'screenshot' in query.lower():
            kk=pyautogui.screenshot()
            kk.save()
        elif 'movie' in query.lower():
            Movie()
        elif 'trailer' in query.lower():
            Trailer()
        else:
            Speak("No command found sir")

TaskExe()
