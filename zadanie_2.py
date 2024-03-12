
from RPi.GPIO import *
import time as t

setmode( BCM)

def allPINlow(dac):
    for pin in dac:
        output(pin, 0)

dac = [8 , 11 , 7, 1, 0, 5, 12, 6]
number = ["11111111", "01111111", "01000000", "00100000", "00000101", "00001000", "00000110"]


for pin in dac:
    setup(pin, OUT)
    output(pin, 0)


for num in number: 
    i = 0
    for pin in dac:
        if num[i] == "1":
            output(pin, 1)
        else:
            output(pin, 0)
        i+=1
    t.sleep(2)
    allPINlow(dac)



allPINlow( dac)


cleanup()