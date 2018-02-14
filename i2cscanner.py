import machine
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
for i in i2c.scan():
    print(hex(i))
