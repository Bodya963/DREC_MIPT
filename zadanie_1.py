from RPi.GPIO import *
import time as t

setmode(BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]


for i in leds:
    setup(i, OUT)
    output( i, 0)

for j in range(3):
    for i in leds:
        output(i, 1)
        t.sleep(0.25)
        output(i, 0)


for pin in leds:
    output(pin, 0)

cleanup()





