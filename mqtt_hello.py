import network
import time
from umqtt.simple import MQTTClient

# Wi-Fi credentials
SSID = "PORTABLE-PI"
PASSWORD = "180294mario"

# MQTT broker details
MQTT_BROKER = "10.9.141.1"
MQTT_PORT = 1883
MQTT_TOPIC = "/home/test"

# Connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())

# Publish MQTT message
def publish_message():
    client = MQTTClient("esp32_client", MQTT_BROKER, port=MQTT_PORT)
    client.connect()
    print("Connected to MQTT broker")
    try:
        while True:
            client.publish(MQTT_TOPIC, "hello from esp32")
            print("Message published to topic:", MQTT_TOPIC)
            time.sleep(5)
    finally:
        client.disconnect()

# Main execution
connect_to_wifi()
publish_message()