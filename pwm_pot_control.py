from machine import Pin, ADC, PWM
from time import sleep_us

# Pin configuration
led_pin = 18
pot_pin = 35

# Initialize PWM for LED
led = PWM(Pin(led_pin), freq=1000, duty=0)

# Initialize ADC for potentiometer
pot = ADC(Pin(pot_pin))
pot.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
pot.width(ADC.WIDTH_10BIT)  # 10-bit resolution (0-1023)

# Constants for fading time
MIN_FADE_TIME = 50  # in microseconds
MAX_FADE_TIME = 500  # in microseconds

while True:
    # Read potentiometer value
    pot_value = pot.read()
    
    # Map potentiometer value to fading time
    fade_time = int(MIN_FADE_TIME + (pot_value / 1023) * (MAX_FADE_TIME - MIN_FADE_TIME))
    
    # LED fading logic
    for duty in range(0, 1024):  # Fade in
        led.duty(duty)
        sleep_us(fade_time)

    for duty in range(1023, -1, -1):  # Fade out
        led.duty(duty)
        sleep_us(fade_time)