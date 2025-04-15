import network
import socket
import neopixel
import machine
import ujson

# Configuration
LED_PIN = 2  # Pin connected to the NeoPixel ring
NUM_LEDS = 16  # Number of LEDs in the NeoPixel ring
SSID = 'PORTABLE-PI'  # Replace with your Wi-Fi SSID
PASSWORD = '180294mario'  # Replace with your Wi-Fi password

# Initialize NeoPixel
np = neopixel.NeoPixel(machine.Pin(LED_PIN), NUM_LEDS)

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        pass
    print('Connected to Wi-Fi:', wlan.ifconfig())

connect_wifi()

# HTML template for the web interface
html = """<!DOCTYPE html>
<html>
<head>
    <title>NeoPixel Control</title>
</head>
<body>
    <h1>NeoPixel Ring Control</h1>
    <form>
        %s
        <button type="submit">Update</button>
    </form>
    <script>
        document.querySelectorAll('input[type=color]').forEach(input => {
            input.addEventListener('input', () => {
                fetch('/update', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({index: input.name, color: input.value})
                });
            });
        });
    </script>
</body>
</html>
"""

# Generate color pickers for each LED
def generate_color_pickers():
    pickers = ""
    for i in range(NUM_LEDS):
        pickers += f'<label for="led{i}">LED {i}</label>'
        pickers += f'<input type="color" id="led{i}" name="{i}" value="#000000"><br>'
    return pickers

# Update NeoPixel colors
def update_neopixel(data):
    index = int(data['index'])
    color = data['color']
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    np[index] = (r, g, b)
    np.write()

# Start the web server
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        try:
            request = cl.recv(1024).decode('utf-8')
            if 'POST /update' in request:
                body = request.split('\r\n\r\n')[1]
                data = ujson.loads(body)
                update_neopixel(data)
                cl.send('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nOK')
            else:
                response = html % generate_color_pickers()
                cl.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + response)
        except Exception as e:
            print('Error:', e)
        finally:
            cl.close()

start_server()