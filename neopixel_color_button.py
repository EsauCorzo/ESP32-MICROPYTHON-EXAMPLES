from machine import Pin
import neopixel
import time

# Configuration
NUM_PIXELS = 30
NEOPIXEL_PIN = 2
BUTTON_PIN = 4
MAX_COLOR_VALUE = 100

# Define 16 colors (RGB values not exceeding MAX_COLOR_VALUE)
COLORS = [
    (MAX_COLOR_VALUE, 0, 0), (0, MAX_COLOR_VALUE, 0), (0, 0, MAX_COLOR_VALUE),
    (MAX_COLOR_VALUE, MAX_COLOR_VALUE, 0), (MAX_COLOR_VALUE, 0, MAX_COLOR_VALUE),
    (0, MAX_COLOR_VALUE, MAX_COLOR_VALUE), (MAX_COLOR_VALUE // 2, MAX_COLOR_VALUE // 2, 0),
    (MAX_COLOR_VALUE // 2, 0, MAX_COLOR_VALUE // 2), (0, MAX_COLOR_VALUE // 2, MAX_COLOR_VALUE // 2),
    (MAX_COLOR_VALUE // 2, MAX_COLOR_VALUE, 0), (MAX_COLOR_VALUE, MAX_COLOR_VALUE // 2, 0),
    (MAX_COLOR_VALUE, 0, MAX_COLOR_VALUE // 2), (0, MAX_COLOR_VALUE, MAX_COLOR_VALUE // 2),
    (MAX_COLOR_VALUE // 2, 0, MAX_COLOR_VALUE), (MAX_COLOR_VALUE // 3, MAX_COLOR_VALUE // 3, MAX_COLOR_VALUE // 3),
    (MAX_COLOR_VALUE // 2, MAX_COLOR_VALUE // 2, MAX_COLOR_VALUE // 2)
]

# Initialize NeoPixel and button
np = neopixel.NeoPixel(Pin(NEOPIXEL_PIN), NUM_PIXELS)
button = Pin(BUTTON_PIN, Pin.IN)

# Current color index
current_color_index = 0

def set_color(color):
    """Set all pixels to the specified color."""
    for i in range(NUM_PIXELS):
        np[i] = color
    np.write()

# Main loop
set_color(COLORS[current_color_index])  # Set initial color
while True:
    if button.value():  # Button pressed
        current_color_index = (current_color_index + 1) % len(COLORS)  # Cycle to next color
        set_color(COLORS[current_color_index])
        time.sleep(0.3)  # Debounce delay