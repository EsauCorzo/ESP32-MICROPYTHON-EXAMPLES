from machine import Pin
from time import sleep

# Configure the button pin
button = Pin(4, Pin.IN, Pin.PULL_UP)  # Replace 0 with your button GPIO pin
counter = 0
previous_state = button.value()

print("Press the button to increase the counter.")

while True:
    current_state = button.value()
    if previous_state == 1 and current_state == 0:  # Detect button press
        counter += 1
        print("Button pressed! Counter:", counter)
    previous_state = current_state
    sleep(0.05)  # Debounce delay