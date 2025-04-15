import network
import time
import dht
import machine
import ujson
from umqtt.simple import MQTTClient
from i2c_lcd import I2cLcd

# WiFi credentials
SSID = "PORTABLE-PI"
PASSWORD = "180294mario"

# MQTT server details
MQTT_SERVER = "10.9.141.1"
MQTT_TOPIC = "/home/test"

# I2C LCD configuration
I2C_ADDR = 0x3F
I2C_SCL = 22
I2C_SDA = 21
LCD_ROWS = 4
LCD_COLS = 20

# DHT22 sensor pin
DHT_PIN = 4

# Connect to WiFi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)
    print("Connected to WiFi:", wlan.ifconfig())

# Initialize DHT22 sensor
dht_sensor = dht.DHT22(machine.Pin(DHT_PIN))

# Initialize I2C and LCD
i2c = machine.I2C(scl=machine.Pin(I2C_SCL), sda=machine.Pin(I2C_SDA))
lcd = I2cLcd(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)

# Connect to WiFi
connect_to_wifi()

# Initialize MQTT client
client = MQTTClient("esp32", MQTT_SERVER)
client.connect()

while True:
    try:
        # Read DHT22 sensor values
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        # Create JSON payload
        payload = ujson.dumps({"temp": temperature, "hum": humidity})

        # Publish to MQTT
        client.publish(MQTT_TOPIC, payload)

        # Display on LCD
        lcd.clear()
        lcd.putstr("Temp: {:.1f} C".format(temperature))
        lcd.move_to(0, 1)
        lcd.putstr("Hum: {:.1f} %".format(humidity))

        # Print to console
        print("Published:", payload)

        # Wait before next reading
        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)