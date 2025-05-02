from machine import ADC, Pin
import time

# Configure ADC on GPIO 34
adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)  # Set attenuation to handle full range (0-3.3V)
adc.width(ADC.WIDTH_12BIT)  # Set 12-bit resolution (0-4095)

while True:
    raw_value = adc.read_u16()  # Read raw ADC value
    adc_value = adc.read()  # Read raw ADC value (0-4095)
    adc_value_mv = adc.read_uv()  # Read raw ADC value in microvolts
    voltage = (adc_value_mv / 1000000)  # Convert microvolts to volts
    print("Raw Value:", raw_value,"ADC value: ", adc_value, "ADC value in microvolts:", adc_value_mv, "Voltage:", voltage, "V")
    time.sleep(0.1)  # Delay for 1 second