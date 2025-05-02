from machine import Pin, ADC
from time import sleep

# Configure LED on GPIO2
led = Pin(23, Pin.OUT)

# Configure potentiometer on ADC pin (e.g., GPIO34)
pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
pot.width(ADC.WIDTH_10BIT)  # 10-bit resolution (0-1023)

while True:
    # Read potentiometer value
    pot_value = pot.read()
    
    # Map potentiometer value to delay range (100ms to 1000ms)
    delay = 100 + (pot_value * 900 // 1023)
    print("Potentiometer value:", pot_value, "Delay:", delay, "ms")
    # Blink LED
    led.value(1)
    sleep(delay / 1000)  # Convert ms to seconds
    led.value(0)
    sleep(delay / 1000)