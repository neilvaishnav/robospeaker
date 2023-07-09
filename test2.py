import win32com.client as wincom

import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = "Hello! I am your robo speaker. How can I assist you?"
speak.Speak(text)

while True:
    x = input("You can type your message here: ")
    if x == 'q':
        time.sleep(2)
        text = "Okk Friends Bye Bye I am going to sleep"
        speak.Speak(text)
        break
    text = f" {x}"
    speak.Speak(text)
