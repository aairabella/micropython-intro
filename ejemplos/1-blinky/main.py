import machine
import time

led = machine.Pin(25, machine.Pin.OUT) # LED on the board

while True:
    if led.value() == 0:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.5)
