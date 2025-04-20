from machine import Pin, ADC
from time import ticks_ms, ticks_diff

# Configure LED on GPIO2
led = Pin(2, Pin.OUT)

# Configure potentiometer on ADC pin (e.g., GPIO34)
pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
pot.width(ADC.WIDTH_10BIT)  # 10-bit resolution (0-1023)

# Initialize timing
last_time = ticks_ms()

while True:
    # Read potentiometer value
    pot_value = pot.read()  # Range: 0-1023

    # Map potentiometer value to delay (e.g., 10ms to 1000ms)
    delay = int(100 + (pot_value / 1023) * 900)

    print("Potentiometer Value:", pot_value, "Delay:", delay)
    # Get current time
    current_time = ticks_ms()

    # Check if the delay has passed
    if ticks_diff(current_time, last_time) >= delay:
        # Toggle LED state
        led.value(not led.value())
        # Update last_time
        last_time = current_time