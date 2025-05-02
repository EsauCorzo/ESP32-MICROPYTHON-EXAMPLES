# ESP32 MicroPython Examples

MicroPython scripts

## Scripts

- [repl_intro](./repl_intro.py): Introduction Script for testing REPL basics
- [blink](./blink.py): Blink LED
- [blink_input](./blink_input.py): Blink LED based on user input
- [button](button.py): Control LED with pushbutton
- [button_pullup](button_pullup.py): Control LED with pushbutton with built in pullup resistor
- [button_toggle](button_toggle.py): Toggle LED while pressing pushbutton
- [button_toggle_not_repeating](button_toggle_not_repeating.py): Toggle LED by pressing pushbutton
- [button_counter](button_counter.py): Count pushbutton presses and turn on LED every 10th press
- [button_counter_irq](button_counter_irq.py): Count pushbutton presses with an interrupt request
- [analog_pot](analog_pot.py): Print ADC value of potentiometer
- [analog_voltage](analog_voltage.py): Different methods of ADC read then convert to voltage value
- [blink_pot_control](blink_pot_control.py): Control blink interval with potentiometer
- [blink_pot_control_tick](blink_pot_control_tick.py): Control blink interval with potentiometer, non blocking
- [analog_ldr](analog_ldr.py): Print ADC value of LDR
- [pwm_led_fade](pwm_led_fade.py): Fade a LED with PWM
- [pwm_pot_control](pwm_pot_control.py): Control the interval of dimming LED with potentiometer
- [pwm_pot_fade](pwm_pot_fade.py): Fade LED with potentiometer
- [pwm_buzzer](pwm_buzzer.py): Play a tone on a passive buzzer using PWM
- [pwm_buzzer_pot](pwm_buzzer_pot.py): Control frequency of passive buzzer with potentiometer, making different tones
- [active_buzzer_beep](active_buzzer_beep.py): beep
- [active_buzzer_pot_beep](active_buzzer_pot_beep.py): Control beep
- [active_buzzer_led_pot_beep](active_buzzer_led_pot_beep.py): Beep with a LED
...and more 

## How to Use

1. Clone this repository to your local machine.
3. Open in VSCode
3. Make sure neccesary modules are in lib folder on ESP32
3. Run desired script on your ESP32 using MicroPico interface

## Requirements

- ESP32 board
- MicroPython firmware installed
- VSCode Installed on your pc
- MicroPico extension installed on VSCode
- Python 3.x installed on your computer