
#from .hw.pifaceGpio import pifaceGpio
from library.hw.dummyGpio import dummyGpio

class gpioFactory(object):

    def __init__(self,hwInterface):

      #  if 'piface' in hwInterface:
          #  self._hwif = pifaceGpio()
       #     pass
        #if 'dummy' in hwInterface:
        self._hwif = hwInterface
        print('dummy',self._hwif)

        self._io = None
        self._direction = None

    def config(self,io,direction):
        self._io = io
        self._direction = direction
        print('Factory',io,direction,self._hwif)
        self._hwif.config(self._io,self._direction)

    def event(self,callback):
        print('Factory', self._io,callback)
        self._hwif.event(self._io,callback)

    def read(self):
        return self._hwif.read(int(self._io))

    def write(self,value):
        print('factory write')
        self._hwif.write(int(self._io),int(value))

