from machine import Pin
import neopixel
import time

# Configuration
NUM_PIXELS = 30  # Number of LEDs in the strip
PIN = 2          # Pin where the NeoPixel is connected
COLOR = (50, 0, 0)  # Red color with brightness 50

# Initialize NeoPixel
np = neopixel.NeoPixel(Pin(PIN), NUM_PIXELS)

def clear_strip():
    """Turn off all LEDs."""
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)
    np.write()

def knight_rider():
    """Simulate Knight Rider LED motion."""
    while True:
        # Move forward
        for i in range(NUM_PIXELS):
            clear_strip()
            np[i] = COLOR
            np.write()
            time.sleep(0.05)
        
        # Move backward
        for i in range(NUM_PIXELS - 2, 0, -1):
            clear_strip()
            np[i] = COLOR
            np.write()
            time.sleep(0.05)

try:
    knight_rider()
except KeyboardInterrupt:
    clear_strip()