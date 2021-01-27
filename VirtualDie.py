# Virtual Die by Scott Webster September 2018
#
# A MicroPython program for the BBC Micro:bit
#
# Press a button to get a randomly chosen die value
# represented as a die face image.
#
from microbit import *
import random
import radio

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

def roll():
    # pick a face at random and
    # show the blank face
    myShowSide = random.randint(1,6)
    display.show(dieSides[0])
    return myShowSide

# Create a seed for that random number generator
random.seed(random.getrandbits(30))
# Default to the blank face
showSide = 0
# Turn on radio
radio.on()
# Loop forever
while(True):
    # Check for incoming message on radio
    incoming = radio.receive()
    if incoming == 'roll':
        # If a roll command is received, call the run() function
        showSide = roll()
        # Take a brief nap to prevent flicker on receiving microbit
        sleep(20)
    elif button_a.is_pressed():
        # If button A is pressed, call the roll() function
        showSide = roll()
    elif button_b.is_pressed():
        # If button B is pressed send the roll command
        # and then call the roll() function
        radio.send('roll')
        showSide = roll()
    else:
        # Display the randomly chosen die face image
        display.show(dieSides[showSide])
