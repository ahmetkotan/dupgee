import network

from utime import sleep_ms


def connect_to_wifi(ssid, password):
    ap = network.WLAN(network.AP_IF)
    ap.active(False)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to wifi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            sleep_ms(500)
            print("Trying connecting to wifi again...")

    print("Connected to wifi.")
    print("Network configuration:", wlan.ifconfig())
