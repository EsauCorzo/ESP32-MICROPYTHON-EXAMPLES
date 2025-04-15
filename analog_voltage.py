from machine import ADC, Pin
import time

# Configure ADC on GPIO 34
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)  # Set attenuation to handle full range (0-3.3V)
adc.width(ADC.WIDTH_12BIT)  # Set 12-bit resolution (0-4095)

while True:
    raw_value = adc.read()  # Read raw ADC value
    voltage = (raw_value / 4095) * 3.3  # Convert to voltage (0-3.3V)
    print("Raw Value:", raw_value, "Voltage:", voltage, "V")
    time.sleep(0.1)  # Delay for 1 second