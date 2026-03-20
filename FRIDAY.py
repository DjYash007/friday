import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import sys
from PyQt5 import QtWidgets, QtCore, QtGui 
from PyQt5.QtCore import QTimer, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from FRIDAYUi import Ui_FridayUI

#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#print(voices[0].id)
#engine.setProperty('voice', voices[0].id)

def speak(audio):
      engine = pyttsx3.init('sapi5')
      voices = engine.getProperty('voices')
      #print(voices[0].id)
      engine.setProperty('voice', voices[0].id)
      engine.say(audio)
      engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else :
        speak("Good Evening!")

    speak("I  am Friday, Please tell! how may I help you")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run (self):
        self.TaskExecution()

    def takeCommand(self):

      r = sr.Recognizer()
      with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)

      try:
          print("Recognizing....")
          query = r.recognize_google(audio, language='en-in')
          print(f"User said: {query}\n")

      except Exception as e:
           #print(e)
            print("Say that again please....")
            return "None"
      query = query.lower()
      return query


    def TaskExecution(self):
        wishMe()
        while True:
            self.query = self.takeCommand()

            if 'wikipedia' in self.query:
                speak("Searching Wikipedia......")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                speak("According to Wikipedia!")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                speak("Opening You Tube")
                webbrowser.open("https://www.youtube.com/")

            elif 'open my class' in self.query:
                speak("Opening Google Meet")
                webbrowser.open("https://meet.google.com/nvf-qprq-dnc")

            elif 'open whatsapp' in self.query:
                speak("Opening Whatsapp")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'open google' in self.query:
                speak("Opening Google")
                webbrowser.open("https://www.google.co.in/webhp?tab=rw&authuser=0")

            elif 'open my mails' in self.query:
                speak("Opening your mails")
                webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

            elif 'what is the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Current time is {strTime}")

            elif 'sing a song' in self.query:
                speak("I have made a song but!; You won't like it!")
                speak('My name is friday..... doo... doo....; My name is friday.... doo.... doo....')
                speak('I will help you..... doo... doo....; I will help you.... doo.... doo....')
                speak('My name is friday..... doo... doo....; My name is friday.... doo....')

            elif 'crack a joke' in self.query:
                speak("What is the strongest animal in the world? ")
                speak("Snail!! as it carries whole home on its back........")
                speak(".........")
                speak("lol!!")

            elif 'you are mad' in self.query:
                speak("That's not nice...")

            elif 'what have you ate' in self.query:
                speak('My stomach is filled by seeing the photos of food on google!!!')

            elif 'what do you think about me' in self.query:
                speak("You are the best in the world!!!. No one is like you!!!!")

            elif 'why is your name friday' in self.query:
                speak("Because, the person, who, built me was a great fan of Iron Man!!!")
                speak(" He got this name from the movie Avengers Endgame!!!")
                speak("In this movie Iron-Man had an AI called FRIDAY that is why my name is FRIDAY!!!")

            elif 'how are you' in self.query:
                speak("I am doing good!!!")

            elif 'i love you' in self.query:
                speak("I know that, but we should know ourselves better")

            elif 'what can you do' in self.query:
                 speak("I can search results on wikipedia, I can open youtube, google \n"
                 "tell you the current time also crack a joke for you")

            elif 'alexa' in self.query:
                  speak("sorry, wrong call")
                  

            elif 'thank you' in self.query:
                speak("YOU'RE WELCOME, HAVE A NICE DAY.")
                sys.exit()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FridayUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("assets/Friday.gif")
        self.ui.Fridayui.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("assets/Loading.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
friday = Main()
friday.show()
sys.exit(app.exec_())
