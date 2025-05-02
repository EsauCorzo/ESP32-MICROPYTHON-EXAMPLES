from machine import Pin
import time

# Configure the LED pin and button pin
led = Pin(18, Pin.OUT)  # Replace 2 with your LED pin number
button = Pin(26, Pin.IN, Pin.PULL_UP)  # Replace 0 with your button pin number

# Variable to track the button state
button_pressed = False

while True:
    if not button.value():  # Button is pressed (active low)
        if not button_pressed:  # Check if it was not already pressed
            led.value(not led.value())  # Toggle the LED
            button_pressed = True  # Mark the button as pressed
    else:
        button_pressed = False  # Reset the button state when released

    time.sleep(0.01)  # Debounce delay