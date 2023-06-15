from microbit import *

clicks = []

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        for click in clicks:
            display.show(Image.ARROW_E)
            sleep(300)
            display.show(click)
            sleep(1000)
    elif button_a.is_pressed():
        clicks.append("A")
    elif button_b.is_pressed():
        clicks.append("B")
    print(clicks)
    sleep(1000)
