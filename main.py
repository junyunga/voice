import speech_recognition as sr

from gtts import gTTS

import os

import time

import playsound


def reply(text, a):
    tts = gTTS(text=text, lang='en')
    print(text)
    filename = 'D:\\' + text + str(a) + '.mp3'

    tts.save(filename)
    playsound.playsound(filename)


def voice_recognition():
    r = sr.Recognizer()
    print('start')

    with sr.Microphone() as source:
        audio = r.listen(source)
        print(source)
        said = " "
        print('ready')

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said


i = 0
list01 = []
answer01 = ''
while True:
    text = voice_recognition()
    print(text)
    if "a" in text:
        answer01 = 'hihihihihihihihihihihihi'
        reply(answer01, i)

        i = i + 1
    elif "bye" in text:
        break

    list01.append(answer01 + str(i - 1) + '.mp3')
