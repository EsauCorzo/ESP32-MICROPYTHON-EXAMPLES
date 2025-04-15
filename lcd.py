from machine import I2C, Pin
from time import sleep
from i2c_lcd import I2cLcd

# ESP32 I2C pins
I2C_SCL = 22  # Change to your SCL pin
I2C_SDA = 21  # Change to your SDA pin

# I2C address of the LCD (usually 0x27 or 0x3F)
I2C_ADDR = 0x3f

# LCD dimensions
LCD_ROWS = 4
LCD_COLS = 20

# Initialize I2C
i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400000)

# Initialize the LCD
lcd = I2cLcd(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)

# Test the LCD
lcd.putstr("Hello, World!\n")
lcd.putstr("MicroPython on\n")
lcd.putstr("ESP32 with I2C\n")
lcd.putstr("20x4 LCD Test")

# Keep the message displayed
while True:
    sleep(1)