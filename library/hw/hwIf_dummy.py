
import time
from threading import Thread
import random
import logging

class raspberry(Thread):

    def __init__(self,logger):
        Thread.__init__(self)

        _libName = str(__name__.rsplit('.',1)[-1])
        self._log = logging.getLogger(logger + '.'+ _libName + '.' + self.__class__.__name__)

        self._log.info('dummy')
        self._callback = None

    def Reset(self):
        return True

    def ConfigIO(self,ioPin,iodir,pullup=None):
        self._log.info('config pin %s , mode %s'%(ioPin,iodir))
        return True

    def WritePin(self,ioPin,value):
        return True

    def ReadPin(self,ioPin):
        value = random.choice([True, False])
        return value

    def Interrupt(self,ioPin,callback,trigger,debounce=100):
        print('GPIO Edge',ioPin, callback, trigger, debounce)
        self._pin = ioPin
        self._callback = callback
#        self.start()
        return True


    def run(self):
        while True:
            time.sleep(30)

            #print('#')
            value = random.choice([True, False])
            self._callback()