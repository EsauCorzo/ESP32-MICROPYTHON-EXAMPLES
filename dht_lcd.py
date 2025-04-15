from machine import Pin, I2C
from time import sleep
from dht import DHT22
from i2c_lcd import I2cLcd

# Initialize DHT22 sensor
dht_pin = Pin(4)  # Use GPIO4 for DHT22 data pin
dht_sensor = DHT22(dht_pin)

# Initialize I2C for LCD
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)  # Adjust pins if necessary
lcd_address = 0x3F  # I2C address of the LCD
lcd = I2cLcd(i2c, lcd_address, 4, 20)  # 20x4 LCD

# Clear LCD
lcd.clear()

while True:
    try:
        # Read data from DHT22
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        # Print temperature and humidity on LCD
        lcd.clear()
        lcd.putstr("Temp: {:.1f}C".format(temperature))  # Line 1
        lcd.move_to(0, 1)
        lcd.putstr("Humidity: {:.1f}%".format(humidity))  # Line 2

        # Wait before next reading
        sleep(2)
    except Exception as e:
        lcd.clear()
        lcd.putstr("Error reading sensor")
        print("Error:", e)
        sleep(2)