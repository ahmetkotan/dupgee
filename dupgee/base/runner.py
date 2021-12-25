try:
    import sys
except Exception as e:
    print(str(e))
    import usys as sys


sys.path.insert(0, "/{{ app_name }}")
sys.path.insert(0, "/{{ app_name }}/dupgee")

from dupgee.wifi import connect_to_wifi
from dupgee.server import run_server


WIFI_SSID = ""
WIFI_PASSWORD = ""


connect_to_wifi(ssid=WIFI_SSID, password=WIFI_PASSWORD)

port = "8080"
if len(sys.argv) > 1:
    port = sys.argv[1]
    if not port.isdigit():
        print("Port number must be a integer.")
        sys.exit(1)

run_server(port=int(port))
