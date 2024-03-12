from RPi.GPIO import *
import time as t
setmode( BCM)

leds = [ 2, 3, 4, 17, 27, 22, 10, 9]

aux = [ 21, 20, 26, 16, 19, 25, 23, 24]

for pin in leds:
    setup( pin, OUT)
    output( pin, 0)

for pin in aux:
    setup( pin , IN)

while True:
    for i in  range(8):
        if input(aux[i]) == 1:
            output( leds[i], 1)
        else:
            output( leds[i], 0)