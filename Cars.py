from microbit import *
import radio

leve_kolo = pin1
prave_kolo = pin2
leve_kolo.set_analog_period(20)
prave_kolo.set_analog_period(20)
full_forward = 1023 * 1.0 / 20
stop = 1023 * 1.5 / 20
full_back = 1023 * 2.0 / 20

radio.on()
radio.config(channel=69)

display.show(Image.ANGRY)
while True:
    sleep(100)
    msg = radio.receive()
    if msg == "vpravo":
        leve_kolo.write_analog(full_back)
        prave_kolo.write_analog(full_back)
    elif msg == "vlevo":
        leve_kolo.write_analog(full_forward)
        prave_kolo.write_analog(full_forward)
    elif msg == "dopredu":
        leve_kolo.write_analog(full_back)
        prave_kolo.write_analog(full_forward)
    else:
        leve_kolo.write_analog(stop)
        prave_kolo.write_analog(stop)
