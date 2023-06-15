from microbit import *
import radio

radio.on()
radio.config(channel=69)
if not compass.is_calibrated():
    compass.calibrate()

path = []
display.show(Image.SKULL)

while True:
    path.append((compass.heading(), accelerometer.get_x(), accelerometer.get_y()))

    if button_a.is_pressed():
        for (angle, x, y) in path:
            radio.send(str(angle)+";"+str(x)+";"+str(y)+";")
            sleep(10)
        display.show(Image.HAPPY)
        sleep(1000)
    print(path)
    sleep(1000)
