import machine
# git clone https://github.com/catdog2/mpy_bme280_esp8266
import bme280
import time

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c, address=0x76)

while True:
    print(bme.values)
    time.sleep_ms(1000)
