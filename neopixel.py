import time
from machine import Pin
import neopixel

# Configuration
NUM_PIXELS = 16  # Number of NeoPixels
PIN_NUM = 2     # Pin connected to the NeoPixel data line

# Initialize NeoPixel
np = neopixel.NeoPixel(Pin(PIN_NUM), NUM_PIXELS)

def clear_pixels():
    """Turn off all pixels."""
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)
    np.write()

def color_wipe(color, delay=50):
    """Fill the strip with a single color, one pixel at a time."""
    for i in range(NUM_PIXELS):
        np[i] = color
        np.write()
        time.sleep_ms(delay)

def rainbow_cycle(delay=20):
    """Display a rainbow cycle across the pixels."""
    for j in range(256):
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // NUM_PIXELS) + j
            np[i] = wheel(pixel_index & 255)
        np.write()
        time.sleep_ms(delay)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

# Main loop
try:
    while True:
        color_wipe((64, 0, 0))  # Red
        color_wipe((0, 64, 0))  # Green
        color_wipe((0, 0, 64))  # Blue
        rainbow_cycle()
except KeyboardInterrupt:
    clear_pixels()
    print("Program stopped.")