import sys
sys.path.append('srcLib')
from unit import Unit
unit = Unit("ssid", "password", "STA")
unit.wifi.connect()
print(unit.wifi.IP)
