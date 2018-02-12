# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()

def WifiConnect(ssid, passwd):
    # Based originally on https://goo.gl/5UMJDr
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to wifi...')
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            pass
    print('Wifi Connected, IP Configuration:', sta_if.ifconfig())
