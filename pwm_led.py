from machine import Pin, PWM
from time import sleep

# Configure GPIO 2 as a PWM pin
led = PWM(Pin(2), freq=1000)

# Function to fade LED in and out
def fade_led():
    while True:
        # Fade in
        for duty in range(0, 1024):
            led.duty(duty)
            sleep(0.001)  # Adjust speed of fading
        # Fade out
        for duty in range(1023, -1, -1):
            led.duty(duty)
            sleep(0.001)

# Start fading
fade_led()