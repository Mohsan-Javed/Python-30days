import time

tim = time.strftime('%H : %M : %S')

if '00 : 00 : 00' < tim < '12 : 00 : 00':
    print ("Good Morning Sir!")

elif '12 : 00 : 00' < tim < '18 : 00 : 00':
    print ("Good Afternoon Sir!")

elif '18 : 00 : 00' < tim < '24 : 00 : 00':
    print ("Good Night Sir!")

timezone = "AM"

if '00 : 00 : 00' < tim < '12 : 00 : 00':
    timezone = "AM"

elif '12 : 00 : 00' < tim < '24 : 00 : 00':
    timezone = "PM"

print (f"Currently, The time is {tim} {timezone}")