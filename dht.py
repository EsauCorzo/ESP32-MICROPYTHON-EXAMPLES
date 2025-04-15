import dht
from machine import Pin
import time

# Initialize DHT sensor (DHT22 or DHT11)
# Replace Pin(2) with the GPIO pin you're using
sensor = dht.DHT22(Pin(4))

while True:
    try:
        # Measure temperature and humidity
        sensor.measure()
        temperature = sensor.temperature()  # Temperature in Celsius
        humidity = sensor.humidity()        # Humidity in percentage

        # Print the values
        print("Temperature: {:.2f}°C".format(temperature))
        print("Humidity: {:.2f}%".format(humidity))

    except OSError as e:
        print("Failed to read sensor:", e)

    # Wait for 2 seconds before the next reading
    time.sleep(2)