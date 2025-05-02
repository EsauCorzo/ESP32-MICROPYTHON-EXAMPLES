from machine import Pin
import time

# Initialize the built-in LED (usually GPIO2 on ESP32)
led = Pin(18, Pin.OUT)

# Get the current time in milliseconds
last_toggle_time = time.ticks_ms()

# Toggle interval in milliseconds
toggle_interval = 500

while True:
    # Get the current time
    current_time = time.ticks_ms()
    
    # Check if the toggle interval has passed
    if time.ticks_diff(current_time, last_toggle_time) >= toggle_interval:
        # Toggle the LED state
        led.value(not led.value())
        # Update the last toggle time
        last_toggle_time = current_time