
import random

class state(object):

    def __init__(self):

        self._closed = 3
        self._opened = 11



    def ConfigIO(self,ioPin,iodir,pullup=None):

        print('config Pin',ioPin)
        return True



    def ReadPin(self,ioPin):
        value = bool(random.getrandbits(1))
       # value = self._gpio.input(ioPin)

        return value



    def start(self):
        self.ConfigIO(self._closed, 'IN', 'UP')
        self.ConfigIO(self._opened, 'IN', 'UP')

    def run(self):
        if (self.ReadPin(self._closed) == 1) and (self.ReadPin(self._opened) == 1):
            print('Moving')
        elif (self.ReadPin(self._closed) == 1) and (self.ReadPin(self._opened) == 0):
            print('OPEN')
        elif (self.ReadPin(self._closed) == 0) and (self.ReadPin(self._opened) == 1):
            print('Closed')
        else:
            print('not found')

if __name__ == "__main__":

    s = state()
    s.start()
    s.run()

