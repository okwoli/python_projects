from time import sleep
import LED 

led = LED.LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
