import board
import analogio

motor=analogio.AnalogOut(board.A0) # MotorReading
pot=analogio.AnalogIn(board.A1) # PotReading
while True:
    speed=pot.value  # CombinesThePreviousStuffToRunTheMotor
    motor.value=speed