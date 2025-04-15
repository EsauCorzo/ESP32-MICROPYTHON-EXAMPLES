import network

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # Create a station interface
    wlan.active(True)  # Activate the interface

    print(f"Connecting to WiFi network: {ssid}")
    wlan.connect(ssid, password)  # Connect to the specified network

    # Wait for connection
    while not wlan.isconnected():
        pass

    print("Connected to WiFi!")
    print("Network config:", wlan.ifconfig())

# Example usage
connect_to_wifi("PORTABLE-PI", "180294mario")
