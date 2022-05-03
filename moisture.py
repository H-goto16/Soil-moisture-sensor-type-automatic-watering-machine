from machine import ADC, Pin
import machine
import utime

soil = ADC(Pin(26))

min_moisture=0
max_moisture=65535
relay_setup = machine.Pin(14, machine.Pin.OUT)
readDelay = 0.5
while True:
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture)
    print(moisture)
    if moisture < 70:
        print("Dirty!")
        relay_setup.value(1)
        utime.sleep(2)
        print(moisture)
    utime.sleep(readDelay)
    relay_setup.value(0)
