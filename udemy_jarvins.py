import datetime, pyttsx3, speech_recognition as sr
import wikipedia, smtplib, webbrowser as wb
import os, pyautogui, psutil
import pyjokes
# import serial
# ser = serial.Serial('COM8', 9600)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is jarvis an AI assistant")

def time():
    time_speak = datetime.datetime.now().strftime("%I:%M:%S")
    speak('The current time is')
    speak(time_speak)


def jokes():
    print(pyjokes.get_jokes())
    speak(pyjokes.get_jokes())


def speak_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day

    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)

# date()

def wishme():
    speak('welcome back sir!')
    time()
    speak_date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak('Good morning sir')
    elif hour >= 12 and hour < 18:
        speak('Good afternoon sir')
    elif hour >= 18 and hour < 24:
        speak("Good evening sir")
    else:
        speak("Goodnight sir")
    speak('Jarvis at your service please tell me how to help you')


def takeCommand():
    """This function takes no arguemnt
    but it takes command from the user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('Please say something..')
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query

def sendEmail(receiver, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('olarindeallitaiwo@gmail.com', 'alli12345')
    server.sendmail('olarindeallitaiwo@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage)
    battery = psutil.sensors_battery()
    print(battery)
    print(battery.percent)
    speak('Your battery pacentage is at ')
    speak(battery.percent)
    


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
        elif 'date' in query:
            speak_date()
        
        elif "wikipedia" in query:
            print('searching wikipedia...')
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak('what do you want to send?')
                content = takeCommand()
                to = 'maxwellolarinde@gmail.com'
                sendEmail(to, content)
                speak('mail sent successfully')
            except Exception as e:
                print(e)
                speak('Unable to send mail')

        elif "search in chrome" in query:

            try:
                speak('what should i search for you sir?')
                chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                searchParameter = takeCommand().lower()
                wb.get(chromePath).open_new(searchParameter + '.com')
                print('searched {} successfully!'.format(searchParameter))
                speak('searched {} successfully!'.format(searchParameter))
                quit()
            except Exception as e:
                pass
        elif 'logout' in query:
            os.system('shutdown -l')
            quit()

        elif 'shutdown' in query:
            print('shutting down the system...')
            speak('shutting down the system.....')
            os.system('shutdown /s /t 1')
            quit()
        elif 'restart' in query:
            print('restarting the system....')
            speak('restarting the system....')
            os.system('shutdown /r /t 1')
            quit()
        elif 'hibernate' in query:
            print('hibernating the system....')
            speak('hibernating the system....')
            os.system('shutdown /h')
            quit()

        elif 'play songs' in query:
            songs_dir = 'C:\\Users\\23480\\Music\\Sheikh Khaleel Husory'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[2]))

        elif 'remember that' in query:
            speak('Please what should i remember?')
            data = takeCommand()
            speak("you told me to read " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            something = open('data.txt', 'r')
            print('you told me to remember that ' + something.read())
            speak("you told me to remember that" + something.read())

        elif 'screenshot' in query:
            screenshot()
            speak('screenshot taken successfully')
            
        elif "processor" in query:
            cpu()

        elif 'jokes' in query:
            jokes()

        # elif 'on' in query:
        #     ser.write(b'Y')

        # elif 'off' in query:
        #     ser.write(b'N')
        
        elif 'offline' in query:
            print('jarvis going offline now.....')
            speak('going offline.....')
            quit()
        
print(psutil.cpu_times())
psutil.disk_usage()