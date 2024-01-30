"""
IR Sensor - STARTER CODE
Engineering 3

"""
# Import libraries
import board
import digitalio
import neopixel 

# Initialize the on-board neopixel and set the brightness.
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

# Set up the IR Sensor using digital pin 2. 
ir_sensor = digitalio.DigitalInOut(board.D2)
ir_sensor.direction = digitalio.Direction.INPUT # Set the IR sensor as an input.
ir_sensor.pull = digitalio.Pull.UP              # Use the internal pull-up resistor.


# While loop runs the code inside continuously. 
while True:
    if ir_sensor.value == False:
        led[0] = (255,0,0)
  

    if ir_sensor.value == True:
        led[0] = (0,255,0)