
import pifacedigitalio

class pifaceGpio(object):

    def __init__(self):
        self._pf = None
        self._event = None

    def config(self,io,direction):
       # self._io = io
        self._pf = pifacedigitalio.PiFaceDigital()

    def event(self,io,callback):
        self._event = self._pf.InputEventListener(chip=pifacedigital)
        self._event.register(io, pifacedigitalio.IODIR_FALLING_EDGE, callback)
        self._event.activate()

    def read(self,io):
        return self._pf.input_pins[io].value
      #  return self._pf.digital_read(io)

    def write(self,io,value):
        print('writeHW',io,value)
   #     self._pf.digital_write(io,value)
        self._pf.output_pins[io].value=value
        return True
