from machine import Pin

# Configure GPIO pins
led = Pin(18, Pin.OUT)  # LED on GPIO 2
button = Pin(26, Pin.IN)  # Button on GPIO 26 

while True:
    # Read button state and set LED state accordingly
    led.value(button.value())  # LED reflects button state