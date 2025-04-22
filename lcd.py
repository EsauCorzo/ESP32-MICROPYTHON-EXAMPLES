from machine import SoftI2C, Pin
from time import sleep
from i2c_lcd import I2cLcd

# ESP32 I2C pins
I2C_SCL = 22  # Change to your SCL pin
I2C_SDA = 21  # Change to your SDA pin

# I2C address of the LCD (usually 0x27 or 0x3F)
I2C_ADDR = 0x27

# LCD dimensions
LCD_ROWS = 2
LCD_COLS = 16

# Initialize I2C
i2c = SoftI2C(scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400000)

# Initialize the LCD
lcd = I2cLcd(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)

# Test the LCD
lcd.putstr(" MicroPython on\n")
lcd.putstr("     ESP32\n")