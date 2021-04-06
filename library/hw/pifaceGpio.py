
import pifacedigitalio

class pifaceGpio(object):

    def __init__(self):
        self._pf = pifacedigitalio.PiFaceDigital()

    def write(self,io,value):
        self._pf.relays[io].value = value

        return True
