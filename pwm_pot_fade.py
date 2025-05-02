from machine import Pin, ADC, PWM
import time

# Configure the potentiometer (ADC) on GPIO34
pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
pot.width(ADC.WIDTH_10BIT)  # 10-bit resolution (0-1023)

# Configure the LED (PWM) on GPIO2
led = PWM(Pin(18))
led.freq(1000)  # Set PWM frequency to 1kHz

while True:
    # Read potentiometer value
    pot_value = pot.read()
    
    # Map potentiometer value (0-1023) to duty cycle (0-1023)
    duty_cycle = pot_value
    
    # Set PWM duty cycle
    led.duty(duty_cycle)
    
    print("Potentiometer Value:", pot_value, "Duty Cycle:", duty_cycle)
    # Small delay to stabilize readings
    time.sleep(0.01)