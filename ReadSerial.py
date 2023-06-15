from microbit import *
import radio

radio.on()
radio.config(channel=69)
display.show(Image.ASLEEP)

while True:
    msg = radio.receive()
    if msg:
        display.show(Image.HAPPY)
        print(msg)
    else:
        display.show(Image.ASLEEP)

    if button_a.was_pressed():
        display.show(Image.ALL_ARROWS)
        print("test")
        sleep(1000)
        display.show(Image.ASLEEP)
