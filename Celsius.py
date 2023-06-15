from microbit import *

while True:
    temperature()
    str(50)
    print(temperature())
    display.clear()
    display.scroll(str(temperature())+ "C")
    sleep(1000)
