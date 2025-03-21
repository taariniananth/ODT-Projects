from machine import Pin, TouchPad, PWM
import time

motor = PWM(Pin(23, mode=Pin.OUT))
motor.freq(50)

threshold=450
capacitiveValue1=0
capacitiveValue2=0
capacitiveValue3=0
capacitiveValue4=0

touch_pin=TouchPad(Pin(4))
touch_pin1=TouchPad(Pin(33))
touch_pin2=TouchPad(Pin(32))
touch_pin3=TouchPad(Pin(15))

led1=Pin(13, Pin.OUT)
led2=Pin(12, Pin.OUT)
led3=Pin(14, Pin.OUT)

led4=Pin(27, Pin.OUT)
led5=Pin(26, Pin.OUT)

led6=Pin(5, Pin.OUT)
led7=Pin(18, Pin.OUT)

while True:
    capacitiveValue1 = touch_pin.read()
    capacitiveValue2 = touch_pin1.read()
    capacitiveValue3 = touch_pin2.read()
    capacitiveValue4 = touch_pin3.read()

    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)
    led7.value(0)


    if capacitiveValue1 < threshold:
        led1.value(1)
        time.sleep(0.1)
        led1.value(0)
        time.sleep(0.1)
        led2.value(1)
        time.sleep(0.1)
        led2.value(0)
        time.sleep(0.1)
        led3.value(1)
        time.sleep(0.1)
        led3.value(0)
        time.sleep(0.1)
        led1.value(1)
        time.sleep(0.1)
        led1.value(0)
        time.sleep(0.1)
        led2.value(1)
        time.sleep(0.1)
        led2.value(0)
        time.sleep(0.1)
        led3.value(1)
        time.sleep(0.1)
        led3.value(0)
        time.sleep(0.2)
        led1.value(1)
        time.sleep(0.1)
        led1.value(0)
        time.sleep(0.1)
        led2.value(1)
        time.sleep(0.1)
        led2.value(0)
        time.sleep(0.1)
        led3.value(1)
        time.sleep(0.1)
        led3.value(0)
        time.sleep(0.1)
        led1.value(1)
        time.sleep(0.1)
        led1.value(0)
        time.sleep(0.1)
        led2.value(1)
        time.sleep(0.1)
        led2.value(0)
        time.sleep(0.1)
        led3.value(1)
        time.sleep(0.1)
        led3.value(0)
        time.sleep(0.2)
        led1.value(1)
        time.sleep(0.1)
        led1.value(0)
        time.sleep(0.1)
        led2.value(1)
        time.sleep(0.1)
        led2.value(0)
        time.sleep(0.1)
        led3.value(1)
        time.sleep(0.1)
        led3.value(0)
        time.sleep(0.1)
        led1.value(1)
        time.sleep(0.1)
        led1.value(0)
        time.sleep(0.1)
        led2.value(1)
        time.sleep(0.1)
        led2.value(0)
        time.sleep(0.1)
        led3.value(1)
        time.sleep(0.1)
        led3.value(0)
        time.sleep(10)


    if capacitiveValue2 < threshold:
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(0.2)
        led4.value(1)
        led5.value(1)
        time.sleep(0.2)
        led4.value(0)
        led5.value(0)
        time.sleep(10)

    if capacitiveValue3 < threshold:
        motor.duty(75)
        time.sleep(0.1)
        motor.duty(15)
        time.sleep(3)

    if capacitiveValue4 < threshold:
        led6.value(1)
        led7.value(1)
        time.sleep(5)
        led6.value(0)
        led7.value(0)
        time.sleep(20)


