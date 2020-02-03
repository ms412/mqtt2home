
import minimalmodbus
import logging

class modbus(object):
    def __init__(self,config,logger):

        _libName = str(__name__.rsplit('.', 1)[-1])
        self._log = logging.getLogger(logger + '.' + _libName + '.' + self.__class__.__name__)

        self._interface = str(config.get('INTERFACE','/dev/ttyUSB0'))
        self._baudrate = int(config.get('BAUDRATE',9800))
        self._deviceID = int(config.get('DEVICEID',0))

        self._if = None


    def setup(self):
        self._log.debug('Methode: setup ()')
        self._if = minimalmodbus.Instrument(self._interface,self._deviceID)
        self._if.serial.baudrate = self._baudrate
        self._if.timeout = 0.8
        self._if.debug = False

    def read(self,data):
        self._log.debug('Methode: read(%s)',data)
     #   print('test',self._if)
        _type,value,size = data
        if 'int' in _type:
           # print('type int',value)
      #      print('read int',value,int(size))
            value = self._if.read_register(int(value,16),int(size))
         #   value = '8'
        elif 'str' in _type:
       #     print('type string',value,size)
          #  value ='TEST'
            value = self._if.read_string(int(value,16),int(size))
        elif 'float' in _type:
            value = self._if.read_float(int(value,16),functioncode=4, numberOfRegisters=2)
        else:
            value = None

        self._log.debug('return value %s', value)
        return value


       # print(typ,value,size)


