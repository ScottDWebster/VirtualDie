# Virtual Die by Scott Webster 9/2018
#
# A MicroPython program for the BBC Micro:bit
#
# Press a button to get a randomly chosen die value
#
from microbit import *
import random
dieSides = ["", "", "", "", "", "", ""]
dieSides[0] = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "00000")
dieSides[1] = Image("00000:"
             "00000:"
             "00900:"
             "00000:"
             "00000")
dieSides[2] = Image("00009:"
             "00000:"
             "00000:"
             "00000:"
             "90000")
dieSides[3] = Image("00009:"
             "00000:"
             "00900:"
             "00000:"
             "90000")
dieSides[4] = Image("90009:"
             "00000:"
             "00000:"
             "00000:"
             "90009")
dieSides[5] = Image("90009:"
             "00000:"
             "00900:"
             "00000:"
             "90009")
dieSides[6] = Image("90009:"
             "00000:"
             "90009:"
             "00000:"
             "90009")
random.seed(random.getrandbits(30))
showSide = 0
while(True):
    if button_a.is_pressed() or button_b.is_pressed():
        showSide = random.randint(1,6)
        display.show(dieSides[0])
    else:
        display.show(dieSides[showSide])
