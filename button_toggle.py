from machine import Pin
import time

# Configure the LED pin (e.g., GPIO2)
led = Pin(18, Pin.OUT)

# Configure the pushbutton pin (e.g., GPIO0)
button = Pin(26, Pin.IN, Pin.PULL_UP)

# Initial LED state
led_state = False

while True:
    # Check if the button is pressed
    if button.value() == 0:  # Button pressed (active low)
        led_state = not led_state  # Toggle LED state
        led.value(led_state)  # Update LED
        time.sleep(0.3)  # Debounce delay