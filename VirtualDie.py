# Virtual Die by Scott Webster September 2018
#
# A MicroPython program for the BBC Micro:bit
#
# Press a button to get a randomly chosen die value
# represented as a die face image.
#
from microbit import *
import random
# Generate a list of empty strings
dieSides = ["", "", "", "", "", "", ""]
# Define the six sides of the die plus a blank one (zero value)
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
# Create a seed for that random number generator
random.seed(random.getrandbits(30))
# Default to the blank face
showSide = 0
# Loop forever
while(True):
    # If either button is pressed pick a face at random and
    # show the blank face
    if button_a.is_pressed() or button_b.is_pressed():
        showSide = random.randint(1,6)
        display.show(dieSides[0])
    else:
        # Display the randomly chosen die face image
        display.show(dieSides[showSide])
