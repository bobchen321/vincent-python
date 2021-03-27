from microbit import *
compass.calibrate()

while True:
    value=compass.heading()
if :(value =<45 and=>314 ):n
    print= (n)
elif:(value =>46 and=<135 ):e
    print= (e)
elif: (value =>136 and=<225):s
    print= (s)
else: (value =>226 and=<313):w
    print= (w)