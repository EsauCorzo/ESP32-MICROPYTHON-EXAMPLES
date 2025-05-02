from machine import Pin, ADC, PWM
import time

# Setup potentiometer on ADC pin
pot = ADC(Pin(35))  # Connect potentiometer to GPIO34 (ADC1 channel 6)
pot.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
pot.width(ADC.WIDTH_10BIT)  # 10-bit resolution (0-1023)

# Setup PWM for buzzer on GPIO18
buzzer = PWM(Pin(18))
buzzer.freq(1000)  # Initial frequency
buzzer.duty(512)  # 50% duty cycle

while True:
    pot_value = pot.read()  # Read potentiometer value (0-1023)
    freq = 100 + int((pot_value / 1023) * 1900)  # Map to frequency range 100-2000 Hz
    buzzer.freq(freq)  # Set buzzer frequency
    time.sleep(.1)  # Small delay to avoid excessive updates