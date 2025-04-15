import network
import socket
from machine import Pin
import neopixel

# Configuration
SSID = 'PORTABLE-PI'
PASSWORD = '180294mario'
NUM_PIXELS = 16  # 4x4 matrix
PIN_NUM = 2  # Pin connected to NeoPixel data line

# Initialize NeoPixel
np = neopixel.NeoPixel(Pin(PIN_NUM), NUM_PIXELS)

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        pass
    print('Connected to Wi-Fi:', wlan.ifconfig())
    return wlan.ifconfig()[0]

# Set NeoPixel colors
def set_color(r, g, b):
    for i in range(NUM_PIXELS):
        np[i] = (r, g, b)
    np.write()

# Web server
def web_server(ip):
    addr = socket.getaddrinfo(ip, 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024).decode('utf-8')
        print('Request:', request)

        # Parse color from request
        if 'GET /?r=' in request:
            try:
                params = request.split(' ')[1].split('?')[1]
                r = int(params.split('&')[0].split('=')[1])
                g = int(params.split('&')[1].split('=')[1])
                b = int(params.split('&')[2].split('=')[1])
                set_color(r, g, b)
            except Exception as e:
                print('Error parsing color:', e)

        # HTML response
        html = """<!DOCTYPE html>
<html>
    <head><title>NeoPixel Control</title></head>
    <body>
        <h1>Control NeoPixel Matrix</h1>
        <form action="/" method="get">
            R: <input type="number" name="r" min="0" max="255" value="0"><br>
            G: <input type="number" name="g" min="0" max="255" value="0"><br>
            B: <input type="number" name="b" min="0" max="255" value="0"><br>
            <button type="submit">Set Color</button>
        </form>
    </body>
</html>
"""
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()

# Main
try:
    ip = connect_wifi()
    web_server(ip)
except KeyboardInterrupt:
    print('Server stopped')