from machine import Pin, PWM
import time

servo = PWM(Pin(5), freq=50)
servo1 = PWM(Pin(18), freq=50)
servo2 = PWM(Pin(21), freq=50)

while True:
    servo.duty(40)
    servo1.duty(40)
    time.sleep(2)

    servo2.duty(40)
    time.sleep(1)
    servo2.duty(90)
    time.sleep(1)

    servo.duty(120)
    servo1.duty(120)
    time.sleep(0.5)
