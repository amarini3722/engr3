
import time
import board
import touchio
import pwmio
from adafruit_motor import servo


pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)


my_servo = servo.ContinuousServo(pwm, min_pulse = 500, max_pulse = 2500)

touch_A4 = touchio.TouchIn(board.A1)  
touch_A5 = touchio.TouchIn(board.A5)  

while True:
    my_servo.throttle = 0.0
    while touch_A4.value:
        my_servo.throttle = 1.0
        time.sleep(.5)
    while touch_A5.value:
        my_servo.throttle = -1.0
        time.sleep(.5)