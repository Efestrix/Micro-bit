from microbit import *

while True:
    if display.read_light_level() > 100:
        display.show(Image.ANGRY)
    sleep(50)
    display.clear()

#display.read_light_level()
