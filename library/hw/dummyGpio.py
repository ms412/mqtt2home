


class dummyGpio(object):

    def __init__(self):
        print('Dummy created',self)
        self._pf = None
        self._event = None

        self._io = {}

    def config(self,io,direction):
       # self._io = io
        #self._pf = pifacedigitalio.PiFaceDigital()
        print('DummyIO ', io, direction)
        pass

    def event(self,io,callback):
        #self._event = self._pf.InputEventListener(chip=pifacedigital)
        #self._event.register(io, pifacedigitalio.IODIR_FALLING_EDGE, callback)
        #self._event.activate()
        print(io,888,callback)
        callback(io)
        pass

    def read(self,io):
        return self._io.get(io,0)

    def write(self,io,value):
        print('writeHW', io, value)
        self._io[io]=value
        return True
