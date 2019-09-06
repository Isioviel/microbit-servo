from microbit import *

'''
Connect a servo motor to pin 16 of the micro:bit
Run this code and press button A until the servo starts to buzz - this is the limit in one direction
Do the same with button B to find the limit in the other direction
'''

position = 50

while True:
    sleep(200)
    print(position)
    pin16.write_analog(position)

    if button_a.was_pressed():
        position -=5

    if button_b.was_pressed():
        position +=5
