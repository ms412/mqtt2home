
#from .hw.pifaceGpio import pifaceGpio
import logging
from library.hw.dummyGpio import dummyGpio

class gpioFactory(object):

    def __init__(self,hwInterface,logger):

        _libName = str(__name__.rsplit('.', 1)[-1])
        self._log = logging.getLogger(logger + '.' + _libName + '.' + self.__class__.__name__)

        self._log.debug('Create gpioFactory Object %s', hwInterface)

      #  if 'piface' in hwInterface:
          #  self._hwif = pifaceGpio()
       #     pass
        #if 'dummy' in hwInterface:
        self._hwif = hwInterface
      #  print('dummy',self._hwif)

        self._io = None
        self._direction = None

    def config(self,io,direction):
        self._log.debug('gpioFactory Config IO: %s; %s'%(io,direction))
        self._io = io
        self._direction = direction
    #    print('Factory',io,direction,self._hwif)
        self._hwif.config(self._io,self._direction)
        return True

    def event(self,callback):
        self._log.debug('gpioFactory Event Register: Callback: %s' % callback)
       # print('Factory', self._io,callback)
        self._hwif.event(self._io,callback)

    def read(self):
        _temp = self._hwif.read(int(self._io))
        self._log.debug('gpioFactory Read %s, %s'%(self._io,_temp))
        return _temp

    def write(self,value):
        #print('factory write')
        self._log.debug('gpioFactory Write %s, %s'%(self._io, value))
        self._hwif.write(int(self._io),int(value))

