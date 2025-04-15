from machine import Pin, PWM
import time

# Configure the servo pin and PWM
servo_pin = Pin(2)  # Change to the pin you connected the servo to
servo = PWM(servo_pin, freq=50)  # 50 Hz for servo control

def set_servo_angle(servo, angle):
    # Map angle (0-180) to duty cycle (40-115 for 50Hz PWM)
    duty = int(40 + (angle / 180) * 75)
    servo.duty(duty)

try:
    while True:
        # Sweep from 0 to 180 degrees
        for angle in range(0, 181, 5):
            set_servo_angle(servo, angle)
            time.sleep(0.05)
        # Sweep back from 180 to 0 degrees
        for angle in range(180, -1, -5):
            set_servo_angle(servo, angle)
            time.sleep(0.05)
except KeyboardInterrupt:
    # Cleanup on exit
    servo.deinit()