import speech_recognition as sr
import sys
import webbrowser
import pyttsx3

# if use only PyAudio
#
# import os
# def talk(words):
#     print(words)
#     os.system("say " + words)
#
# talk("Hello, ask me something")


def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk('Hello, ask me something')


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk('Say')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio).lower()  # language="ru-RU"
        talk('You say: ' + task)
    except sr.UnknownValueError:
        talk('I don\'t understand you.')
        task = command()

    return task


def make_something(task):
    if 'open google' in task:
        talk('Already opening')
        url = 'https://www.google.com'
        webbrowser.open(url)
    elif 'what is your name' in task:
        talk('My name is Sonya')
    elif 'bye' in task:
        talk('Bye, see you later')
        sys.exit()


while True:
    make_something(command())
