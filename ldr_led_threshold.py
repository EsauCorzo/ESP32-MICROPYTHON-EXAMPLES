from machine import Pin, ADC
import time

# Initialize LDR on GPIO34 (ADC1 channel 6)
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
ldr.width(ADC.WIDTH_10BIT)  # 10-bit resolution (0-1023)

# Initialize LED on GPIO2
led = Pin(18, Pin.OUT)

# Function to read min and max LDR values
def calibrate_ldr(duration=5):
    print("Calibrating... Move the LDR to light and dark conditions.")
    min_val = 1023
    max_val = 0
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duration * 1000:
        value = ldr.read()
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
        time.sleep(0.1)
    print(f"Calibration complete. Min: {min_val}, Max: {max_val}")
    return min_val, max_val

# Main function
def main():
    min_val, max_val = calibrate_ldr(10)  # Calibrate for 10 seconds
    threshold_on = (max_val - min_val) * 0.7 + min_val  # 70% of the range
    threshold_off = (max_val - min_val) * 0.3 + min_val  # 30% of the range

    print(f"Threshold ON: {threshold_on}, Threshold OFF: {threshold_off}")

    while True:
        ldr_value = ldr.read()
        print(f"LDR Value: {ldr_value}")
        if ldr_value > threshold_on:
            led.value(0)  # Turn LED on
        elif ldr_value < threshold_off:
            led.value(1)  # Turn LED off
        time.sleep(0.1)

# Run the program
main()