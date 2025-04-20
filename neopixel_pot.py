from machine import Pin, ADC
import neopixel

# Configuration
NEOPIXEL_PIN = 2
POTENTIOMETER_PIN = 34
NUM_PIXELS = 30

# Initialize NeoPixel strip
np = neopixel.NeoPixel(Pin(NEOPIXEL_PIN), NUM_PIXELS)

# Initialize potentiometer (ADC)
pot = ADC(Pin(POTENTIOMETER_PIN))
pot.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
pot.width(ADC.WIDTH_10BIT)  # 10-bit resolution (0-1023)

def map_value(value, in_min, in_max, out_min, out_max):
    """Map a value from one range to another."""
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    # Read potentiometer value
    pot_value = pot.read()
    
    # Map potentiometer value to number of pixels
    num_lit_pixels = map_value(pot_value, 0, 1023, 0, NUM_PIXELS)
    
    # Light up only the last LED according to the ADC value
    last_led_index = map_value(pot_value, 0, 1023, 0, NUM_PIXELS - 1)
    for i in range(NUM_PIXELS):
        if i == last_led_index:
            np[i] = (0, 0, 50)  # Blue color
        else:
            np[i] = (0, 0, 0)  # Turn off

    # # Update NeoPixel strip
    # for i in range(NUM_PIXELS):
    #     if i < num_lit_pixels:
    #         np[i] = (0, 0, 50)  # Blue color
    #     else:
    #         np[i] = (0, 0, 0)  # Turn off


    np.write()