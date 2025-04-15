import network

def wifi_scan():
    wlan = network.WLAN(network.STA_IF)  # Create a station interface
    wlan.active(True)  # Activate the interface

    print("Scanning for WiFi networks...")
    networks = wlan.scan()  # Perform a scan for available networks

    for net in networks:
        ssid = net[0].decode('utf-8')  # Network name
        bssid = ':'.join(f'{b:02x}' for b in net[1])  # MAC address
        channel = net[2]  # Channel
        rssi = net[3]  # Signal strength
        authmode = net[4]  # Authentication mode
        hidden = net[5]  # Hidden SSID flag

        print(f"SSID: {ssid}, BSSID: {bssid}, Channel: {channel}, RSSI: {rssi}, AuthMode: {authmode}, Hidden: {hidden}")

# Run the WiFi scan
wifi_scan()
