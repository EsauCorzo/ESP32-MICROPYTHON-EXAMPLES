from machine import Pin

# Initialize LED on GPIO 18
led = Pin(18, Pin.OUT)

# Main loop
while True:
    # Prompt user for input
    command = input("Enter 'ON' or '1' to turn on, 'OFF' or '0' to turn off the LED: ").strip().upper()
    
    if command in ["ON", "1"]:
        led.value(1)
        print("LED is now ON.")
    elif command in ["OFF", "0"]:
        led.value(0)
        print("LED is now OFF.")
    else:
        print("Invalid input. Please enter 'ON', '1', 'OFF', or '0'.")