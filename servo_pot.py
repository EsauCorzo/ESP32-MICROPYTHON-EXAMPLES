from machine import ADC, Pin
from servo import Servo

# Initialize the servo on pin X1 (adjust as needed)
servo = Servo(2)  # Servo 2 corresponds to pin 2 on esp32

# Initialize the potentiometer on ADC pin
pot = ADC(Pin(34))  # Use GPIO 34 for the potentiometer (adjust as needed)
pot.atten(ADC.ATTN_11DB)  # Configure for full range (0-3.3V)

# Map function to convert potentiometer value to servo angle
def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    # Read potentiometer value
    pot_value = pot.read()  # Read ADC value (0-4095)
    
    # Map potentiometer value to servo angle (0-180 degrees)
    angle = map_value(pot_value, 0, 4095, 0, 180)
    
    # Print the potentiometer value and corresponding angle

    print("Potentiometer Value:", pot_value, "Mapped Angle:", angle)
    
    # Set servo angle
    servo.move(angle)