from servo import Servo
import time

# Initialize the servo on pin D2 (adjust pin as needed)
servo = Servo(2)  # Replace 2 with the correct pin number for your setup

def set_servo_angle():
    while True:
        try:
            # Get user input from REPL
            angle = input("Enter servo angle (0 to 180 degrees, or 'exit' to quit): ")
            
            if angle.lower() == 'exit':
                print("Exiting...")
                break
            
            # Convert input to integer
            angle = int(angle)
            
            # Validate angle range
            if 0 <= angle <= 180:
                servo.move(angle)  # Set servo to the specified angle
                print(f"Servo moved to {angle} degrees.")
            else:
                print("Invalid angle. Please enter a value between 0 and 180.")
        
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'exit'.")

# Run the function
set_servo_angle()