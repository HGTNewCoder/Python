import pyttsx3
import speech_recognition
import wikipedia
from datetime import date
from datetime import datetime

robot_mouth = ""
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
today = date.today()
time = datetime.now()
engine = pyttsx3.init() # initialize

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: Listening!")
        audio = robot_ear.record(mic, duration = 5)
        print("Robot: ...")

    try:
        User = robot_ear.recognize_google(audio)
        print("You:" + User)
    except:
        User = ""
        print("You: " + User)
        print("Robot: I don't understand what you said")
        
    if "hello" in User:
        robot_mouth = "hi there"
    elif "how are you" in User:
        robot_mouth = "i'm fine"
    elif "today" in User:
        robot_mouth = today.strftime("%B, %d, %Y")
    elif "time" in User:
        robot_mouth = time.strftime("%H hours %M minutes")
    elif User == "":
        robot_mouth = "i don't understand what you've said"
    elif "bye" in User:
        robot_mouth = "Bye"
        engine.say(robot_mouth)
        engine.runAndWait()
        print("Bye!")
        break
    elif "feel" in User:
        robot_mouth = "I'm OK"
    elif "Donald Trump":
        robot_mouth = wikipedia.summary("Donald Trump", sentences = 1)
    print("Robot: " + robot_brain)
    engine.say(robot_mouth)
    engine.runAndWait()