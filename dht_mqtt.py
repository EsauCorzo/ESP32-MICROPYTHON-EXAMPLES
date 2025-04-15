import time
import dht
from machine import Pin
import network
import ujson
from umqtt.simple import MQTTClient

# Wi-Fi credentials
WIFI_SSID = 'PORTABLE-PI'
WIFI_PASSWORD = '180294mario'

# MQTT server details
MQTT_SERVER = '10.9.141.1'
MQTT_PORT = 1883
MQTT_TOPIC = '/home/test'

# Initialize DHT sensor
dht_sensor = dht.DHT22(Pin(4))  # Use the appropriate GPIO pin

# Connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to Wi-Fi:', wlan.ifconfig())

# Publish data to MQTT
def publish_to_mqtt(client, temperature, humidity):
    payload = ujson.dumps({"temp": temperature, "hum": humidity})
    client.publish(MQTT_TOPIC, payload)
    print('Published:', payload)

# Main function
def main():
    connect_to_wifi()
    client = MQTTClient('esp32_dht', MQTT_SERVER, port=MQTT_PORT)
    client.connect()
    print('Connected to MQTT server')

    while True:
        try:
            dht_sensor.measure()
            temperature = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            publish_to_mqtt(client, temperature, humidity)
        except Exception as e:
            print('Error:', e)
        time.sleep(10)  # Adjust the delay as needed


main()