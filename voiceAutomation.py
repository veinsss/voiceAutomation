import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import keyboard
import subprocess

userMic = sr.Recognizer()
engineTtx = pyttsx3.init()


with sr.Microphone() as source:
    while True:
        print("Waiting for key prompt --> CTRL + ALT + S")

        #keyboard.wait("ctrl+alt+s")

        print("Currently Listening...")

        audio_data = userMic.listen(source, phrase_time_limit=5)
        print("Listening harder...")

        temp = userMic.recognize_google(audio_data)
        print(f"You have said {temp}")

        # if i say search and it comes out to true it would proceeed to search what I say after search
        if "search for" in temp.lower():
            searchQuery = temp.lower().split("search")[-1].strip()

            engineTtx.say(f"you have searched for {searchQuery}")
            engineTtx.runAndWait()
            url = f"https://www.google.com/search?q={searchQuery}"
            webbrowser.open_new_tab(url)

        if "say" in temp.lower():
            say = temp.lower().split("search")[-1]

            tempString = " " 
            tempString.join(say)

            engineTtx.say({say})
            engineTtx.runAndWait()


        if "open chrome" in temp.lower():
            os.system(r"C:\Progra~1\Google\Chrome\Application\chrome.exe")
            print("SUCCESS")
