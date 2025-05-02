from machine import Pin, PWM
from time import sleep

# Configure PWM on GPIO18
buzzer = PWM(Pin(18))

# Function to play a tone
def play_tone(frequency, duration):
    buzzer.freq(frequency)  # Set frequency
    buzzer.duty(512)        # Set duty cycle (50%)
    sleep(duration)         # Play for the specified duration
    buzzer.duty(0)          # Turn off the buzzer

while True:
    play_tone(1000, 0.5)  # Play 1kHz tone for 0.5 seconds
    sleep(0.5)            # Pause for 0.5 seconds
    play_tone(1500, 0.5)  # Play 1.5kHz tone for 0.5 seconds
    sleep(0.5)            # Pause for 0.5 seconds