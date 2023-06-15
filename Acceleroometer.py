from microbit import *
import random

answers = ["da", "are u drunk", "just do it", "nope", "am i joking to u"]

while True:
    if accelerometer.is_gesture("shake"):
        display.scroll(random.choice(answers))
        sleep(2000)
        display.clear()
