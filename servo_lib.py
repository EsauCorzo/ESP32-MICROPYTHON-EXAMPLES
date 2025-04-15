from servo import Servo
import time

# Initialize the servo on pin gpio (adjust pin as needed)
servo = Servo(2)  # Servo(1) corresponds to pin gpio2 on esp32

def sweep_servo():
    while True:
        # Sweep from 0 to 180 degrees
        for angle in range(0, 181, 5):  # Increment by 5 degrees
            servo.move(angle)
            time.sleep_ms(50)  # 50ms delay between steps
        
        # Sweep back from 180 to 0 degrees
        for angle in range(180, -1, -5):  # Decrement by 5 degrees
            servo.move(angle)
            time.sleep_ms(50)  # 50ms delay between steps

# Start sweeping the servo
sweep_servo()