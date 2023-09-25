import time
import digitalio
import board

photo=digitalio.DigitalInOut
tim=time.monotonic()
number=0

while True:
    print("test")
    if(tim + 4) < time.monotonic():
        print("ready.")
        print(number)
        tim=time.monotonic()
    if(photo==True):
        number=number+1
