
import threading
import logging
from library.gpio import gpio

class led(object):
    def __init__(self, gpio):

        super.__init__(gpio,'OUT')

    def on(self):
        super.set(True)
        return super.get()

    def off(self):
        super.set(False)
        return super.get()

class colorLed(object):

