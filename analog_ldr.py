from machine import ADC, Pin
import time

# Configure ADC for GPIO34
ldr_pin = ADC(Pin(34))
ldr_pin.atten(ADC.ATTN_11DB)  # Set attenuation to read full 0-3.3V range
ldr_pin.width(ADC.WIDTH_12BIT)  # Set 12-bit resolution

while True:
    ldr_value = ldr_pin.read()  # Read the analog value
    print("LDR Value:", ldr_value)
    time.sleep(0.1)  # Delay for 1 second