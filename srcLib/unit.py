import network
import time
import sys
sys.path.append('/srcLib')

class Unit:
    class Wifi:
        class WifiMode:
            AP = "AP"
            STA = "STA"

        @staticmethod
        def isCorrectStr(val):
            return isinstance(val, str) and len(val) > 0 and " " not in val

        def __init__(self, ssid, password, mode):
            self.__ssid = ssid
            self.__password = password
            self.__mode = mode

        @property
        def ssid(self):
            return self.__ssid

        @ssid.setter
        def ssid(self, ssid):
            if self.isCorrectStr(ssid):
                self.__ssid = ssid
            else:
                print("недопустимое значение")

        @property
        def password(self):
            return self.__password

        @password.setter
        def password(self, password):
            if self.isCorrectStr(password) and len(password) > 8:
                self.__password = password
            else:
                print("недопустимое значение")

        @property
        def mode(self):
            return self.__mode

        @mode.setter
        def mode(self, mode):
            if mode in [Unit.Wifi.WifiMode.AP, Unit.Wifi.WifiMode.STA]:
                self.__mode = mode
            else:
                print("недопустимое значение")

        def connect(self):
            if self.__mode == Unit.Wifi.WifiMode.STA:
                wlan = network.WLAN(network.STA_IF)
                wlan.active(True)
                while wlan.isconnected() is False:
                    wlan.connect(self.__ssid, self.__password)
                    time.sleep(1)
            elif self.__mode == Unit.Wifi.WifiMode.AP:
                wlan = network.WLAN(network.AP_IF)
                wlan.active(True)
                wlan.config(essid=self.__ssid, password=self.__password)
        @property
        def IP(self):
            return (network.WLAN(network.STA_IF).ifconfig()[0])

    def __init__(self, ssid, password, wifiMode):
        self.wifi = Unit.Wifi(ssid, password, wifiMode)



    

