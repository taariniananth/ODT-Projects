import machine
import time

# Set up the GPIO pins for the stepper motor
in1 = machine.Pin(14, machine.Pin.OUT)
in2 = machine.Pin(27, machine.Pin.OUT)
in3 = machine.Pin(26, machine.Pin.OUT)
in4 = machine.Pin(25, machine.Pin.OUT)
stepDuration=0.005

while(True):
    in1.value(1)l
    in2.value(0)
    in3.value(0)
    in4.value(0)
    time.sleep(stepDuration)

    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(0)
    time.sleep(stepDuration)

    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    time.sleep(stepDuration)

    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    time.sleep(stepDuration)





