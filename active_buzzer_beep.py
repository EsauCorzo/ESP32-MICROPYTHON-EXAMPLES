from machine import Pin
from time import sleep_ms

# Configure GPIO23 as an output pin
buzzer = Pin(23, Pin.OUT)

while True:
    # Turn the buzzer on
    buzzer.on()
    sleep_ms(50)  # Beep for 50ms
    # Turn the buzzer off
    buzzer.off()
    sleep_ms(5000)  # Wait for 5 seconds