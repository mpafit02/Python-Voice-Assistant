import os
import time
import random
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    r1 = random.randint(1, 10000000)
    r2 = random.randint(1, 10000000)

    # Transform text to audio
    tts = gTTS(text=str(text), lang="en")

    # Save the text converted to audio in the file
    filename = str(r2)+"voice"+str(r1) + ".mp3"
    tts.save(filename)

    # Play the voice that we have record
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    # Listen audio from the microphone
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        # Try to recognize what we have said
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
            speak("Sorry, I din't get that.")

    return said


def main():
    speak("Voice assistant, at your service!")
    repeat = True
    while repeat:
        text = get_audio()

        if "hello" in text:
            speak("Hello Marios.")
        elif "what is your name" in text:
            speak("My name is assistant.")
        elif "goodbye" in text:
            speak("Bye Marios.")
            repeat = False
        else:
            speak("Sorry, I din't get that.")


main()
