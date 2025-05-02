from machine import Pin, PWM
from time import sleep

# Configure GPIO 2 as a PWM pin
led = PWM(Pin(18), freq=1000)

while True:
    # Fade in
    for duty in range(0, 1024):
        led.duty(duty)
        sleep(0.001)  # Adjust speed of fading
    # Fade out
    for duty in range(1023, -1, -1):
        led.duty(duty)
        sleep(0.001)