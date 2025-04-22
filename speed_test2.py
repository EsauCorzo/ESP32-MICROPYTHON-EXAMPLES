import time

total_calculations = 0
calculations = 0

print("Iniciando MicroPython Test...")

for second in range(1, 4):
    calculations = 0
    start_time = time.ticks_ms()
    end_time = time.ticks_add(time.ticks_ms(), 1000)
    
    while time.ticks_diff(end_time, time.ticks_ms()) > 0:
        result = (1234.56 * 7890.12) / 345.67
        calculations += 1
    
    total_calculations += calculations
    print(f"Total en segundo {second}: {calculations}")

print(f"Total en 3 segundos: {total_calculations}")