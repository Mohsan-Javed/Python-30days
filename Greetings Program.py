import time
import pyttsx3

engine = pyttsx3.init()

tim = time.strftime('%H : %M : %S')

timezone = "AM"

if '00 : 00 : 00' < tim < '12 : 00 : 00':
    timezone = "AM"

elif '12 : 00 : 00' < tim < '24 : 00 : 00':
    timezone = "PM"

if '00 : 00 : 00' < tim < '12 : 00 : 00':
    engine.say(f"Good Morning Sir! Currently, The time is {tim} {timezone}")
    engine.runAndWait()

elif '12 : 00 : 00' < tim < '18 : 00 : 00':
    engine.say(f"Good Afternoon Sir! Currently, The time is {tim} {timezone}")
    engine.runAndWait()

elif '18 : 00 : 00' < tim < '24 : 00 : 00':
    engine.say(f"Good Evening Sir! Currently, The time is {tim} {timezone}")
    engine.runAndWait()