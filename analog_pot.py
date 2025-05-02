from machine import ADC, Pin
import time

# Configure ADC on pin 34
adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)  # Set attenuation to read full 0-3.3V range
adc.width(ADC.WIDTH_12BIT)  # Set 12-bit resolution

while True:
    analog_value = adc.read()  # Read the analog value
    print("Analog Value:", analog_value)
    time.sleep(0.01)  # Delay for 500ms