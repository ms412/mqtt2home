
from library.bitoperation import bitoperation

import time
import random
import logging
import RPi.GPIO as GPIO

from threading import Thread


'''
Pin     Numbers    RPi.GPIO    Raspberry Pi Name    BCM2835
P1_01    1             3V3
P1_02    2             5V0
P1_03    3             SDA0         GPIO0
P1_04    4             DNC
P1_05    5             SCL0         GPIO1
P1_06    6             GND
P1_07    7             GPIO7        GPIO4
P1_08    8             TXD          GPIO14
P1_09    9             DNC
P1_10    10            RXD          GPIO15
P1_11    11            GPIO0        GPIO17
P1_12    12            GPIO1        GPIO18
P1_13    13            GPIO2        GPIO21
P1_14    14            DNC
P1_15    15            GPIO3        GPIO22
P1_16    16            GPIO4        GPIO23
P1_17    17            DNC
P1_18    18            GPIO5        GPIO24
P1_19    19            SPI_MOSI     GPIO10
P1_20    20            DNC
P1_21    21            SPI_MISO     GPIO9
P1_22    22            GPIO6        GPIO25
P1_23    23            SPI_SCLK     GPIO11
P1_24    24            SPI_CE0_N    GPIO8
P1_25    25            DNC
P1_26    26            SPI_CE1_N    GPIO7
'''

class raspberry(object):

    def __init__(self, logger):

        _libName = str(__name__.rsplit('.',1)[-1])
        self._log = logging.getLogger(logger + '.'+ _libName + '.' + self.__class__.__name__)
        #define log object
        self._gpio = GPIO
       # self._gpio.setmode(GPIO.BCM)
        GPIO.setmode(GPIO.BOARD)
        self._gpio.setwarnings(False)


    def __del__(self):
        self._gpio.cleanup()

    def ConfigIO(self,ioPin,iodir,pullup=None):
     #   print(ioPin,iodir,pullup)

        if 'IN' in iodir:
            if 'UP' in pullup:
                self._gpio.setup(ioPin, self._gpio.IN, pull_up_down=self._gpio.PUD_UP)
            else:
                self._gpio.setup(ioPin, self._gpio.IN, pull_up_down=self._gpio.PUD_DOWN)
        else:
            #self._gpio.setup(ioPin,self._gpio.OUT, initial=self._gpio.HIGH)
            self._gpio.setup(ioPin,self._gpio.OUT)
        return True

    def WritePin(self,ioPin,value):

        self._gpio.output(ioPin, value)
        return True

    def ReadPin(self,ioPin):
        value = self._gpio.input(ioPin)
   #     print(value)

        return value

    def Interrupt(self,ioPin,callback,trigger,debounce=100):

        if 'FALLING' in trigger:
            self._gpio.add_event_detect(ioPin,self._gpio.FALLING,callback=callback,bouncetime=debounce)
        elif 'RISING' in trigger:
            self._gpio.add_event_detect(ioPin, self._gpio.RISING, callback=callback, bouncetime=debounce)
        else:
            self._gpio.add_event_detect(ioPin, self._gpio.BOTH, callback=callback, bouncetime=debounce)
        return True


