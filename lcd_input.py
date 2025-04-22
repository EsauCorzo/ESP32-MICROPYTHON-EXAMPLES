from machine import SoftI2C, Pin
from i2c_lcd import I2cLcd

# I2C configuration
I2C_ADDR = 0x27  # Change this if your LCD has a different address
I2C_SCL = 22     # GPIO pin for SCL
I2C_SDA = 21     # GPIO pin for SDA

# Initialize I2C
i2c = SoftI2C(scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400000)

# Initialize LCD
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)  # 2 rows, 16 columns

# Clear the LCD
lcd.clear()

# Function to print input to the LCD
def print_to_lcd():
    while True:
        # Get user input from REPL
        text = input("Enter text to display: ")
        line = input("Enter line number (1 or 2): ")

        # Validate line number
        if line not in ['1', '2']:
            print("Invalid line number. Please enter 1 or 2.")
            continue

        # Convert line to integer and adjust for 0-based indexing
        line = int(line) - 1

        # Clear the specified line
        lcd.move_to(0, line)
        lcd.putstr(" " * 16)

        # Print text to the specified line
        lcd.move_to(0, line)
        lcd.putstr(text[:16])  # Truncate text to fit the LCD

        print(f"Text '{text}' printed on line {line + 1}.")

# Run the function
print_to_lcd()