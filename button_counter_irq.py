from machine import Pin
from time import ticks_ms, ticks_diff

# Pin configuration
button_pin = 26
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

# Variables for debounce and press count
debounce_time = 250  # 100ms debounce time
last_press_time = 0
press_count = 0

def button_handler(pin):
    global last_press_time, press_count
    current_time = ticks_ms()
    if ticks_diff(current_time, last_press_time) > debounce_time:
        last_press_time = current_time
        press_count += 1
        print("Button pressed! Count:", press_count)

# Attach interrupt to the button pin
button.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Keep the program running
while True:
    pass
