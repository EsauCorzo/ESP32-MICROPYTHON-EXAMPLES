from machine import Pin

# Configure GPIO pins
led = Pin(2, Pin.OUT)  # LED on GPIO 2
button = Pin(4, Pin.IN, Pin.PULL_UP)  # Button on GPIO 4 with pull-up resistor

while True:
    # Read button state and set LED state accordingly
    led.value(not button.value())  # LED reflects button state (inverted due to pull-up)