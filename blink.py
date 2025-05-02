from machine import Pin
from time import sleep

led = Pin(18, Pin.OUT)  # Initialize GPIO pin 2 as output for the LED

while True:
    led.on()  # Turn the LED on
    sleep(1)   # Wait for 1 second
    led.off()  # Turn the LED off
    sleep(1)   # Wait for 1 second