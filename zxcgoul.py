import RPi.GPIO as IO
import time as t

import matplotlib.pyplot as plt

dac = [ 8, 11 ,7, 1, 0, 5, 12, 6 ]
led = [2, 3, 4, 17,  27,  22,  10, 9]

IO.setmode(IO.BCM)

IO.setup( dac, IO.OUT)
IO.setup( led, IO.OUT)

comp = 14 #выход компоратора 
IO.setup(comp, IO.IN)

OUTzxc = 13  #  GPIO  тройки модуля 
IO.setup(OUTzxc, IO.OUT, initial = 0)

def setdac( bi):
    for i in range(8):
        IO.output(dac[i], int(bi[i]))
    return


# Функция получиния с АЦП
def adc():
    bi = "00000000"
    for i in range(8):
        bi =  bi[:i] + '1' + bi[i+1:]
        setdac( bi)
        t.sleep( 0.003)
        if IO.input(comp) == 1:
            bi = bi[:i] + '0'+ bi[i+1:]
    return int(bi, 2)


try:
    data = []
    countn = 0
    with open( "data.txt", 'w') as f:
        IO.output( OUTzxc, 1)
        t_start = t.time()
        while True:
            dzxc = adc()
            data.append(dzxc)
            countn+=1
            

            if dzxc > 240 :
                IO.output( OUTzxc, 0)
                break

        while True:
            dzxc = adc()
            data.append(dzxc)
            countn+=1
            

            if dzxc < 50:
                t_stop = t.time()
                break

        plt.plot(data)
        plt.show()
    

        f.write('\n'.join([str(i) for i in data]) )

        with open( "setting.txt", "w") as f:
            f.write( " частота дискретизации = " + str( countn / (t_stop - t_start)))
            f.write( " \n время измерений = "+ str( t_stop - t_start))

            
             


        
        

         
finally:
    IO.cleanup()