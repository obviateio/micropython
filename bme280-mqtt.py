import machine
# git clone https://github.com/catdog2/mpy_bme280_esp8266
import bme280
import time
from umqtt.simple import MQTTClient

# Requires the use of wificlient-boot.py as boot.py
# Configure the following two lines. Username & API key from io.adafruit.com
conf = {'deviceid':'ESP8266','user':'USERNAMEHERE','apikey':'APIKEYHERE'}
WifiConnect('WIFISSID', 'WIFIPASSWORD') 

# Setup the connection to the BME280
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

while True:
    # Setup the MQTT connection to Adafruit
    c = MQTTClient(conf['deviceid'], server="io.adafruit.com", user=conf['user'], password=conf['apikey'], port=1883) 
    c.connect()

    # Grab the latest enviromental values
    envi = bme.values
    print(envi)

    # Publish all the values via MQTT
    c.publish(conf['user']+"/feeds/temp", envi[0])
    c.publish(conf['user']+"/feeds/pres", envi[1])
    c.publish(conf['user']+"/feeds/humid", envi[2])

    # Disconnect from MQTT And goto sleep
    c.disconnect()
    time.sleep_ms(10000) #10k mili = 10 seconds
