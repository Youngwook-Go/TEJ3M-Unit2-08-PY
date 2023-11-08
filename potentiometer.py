import time
import board
import pwmio
from analogio import AnalogIn
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP0, frequency=50)
potentiometer = AnalogIn(board.GP26)

my_servo = servo.ContinuousServo(pwm)

while True:
    try:
        # change range of potentiometer(0 to 65536) into range of servo throttle( -1 to 1)
        servoValue = potentiometer.value / (65536 / 2) - 1 
        print("Potentiometer: " + str(servoValue))
        
        my_servo.throttle = servoValue
        
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.2)
