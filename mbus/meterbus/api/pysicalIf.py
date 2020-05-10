
import serial
import time
from datetime import datetime



class serialIf(object):

    def __init__(self):

        self._if = None
        self._nodeId = 0x10

    def _printNice(self, frame):
        print(len(frame))
        n = ''
        for x in frame:
            print(x)
            n = n + ',' + "".join('{:02x}'.format(x))

        return n


    def _inter_byte_timeout(self,baudrate):
        definition = {
            300: 0.12,
            600: 0.60,
            1200: 0.4,
            2400: 0.2,
            4800: 0.2,
            9600: 0.1,
            19200: 0.1,
            38400: 0.1,
        }

        return definition.get(baudrate, None)

    def _checksum(self,body):
        _temp = 0
        for item in body:
            _temp = _temp + item
      #  print('checksum',x)
        return _temp % 256

    def connect(self,device,baudrate):
        ibt = self._inter_byte_timeout(baudrate)
        try:
            self._if = serial.serial_for_url(device,baudrate,8,'E',1,inter_byte_timeout=ibt,timeout=1)

        except serial.serialutil.SerialExecption as e:
            print(e)

    def mbusWrite(self,data):
        self._if.write(bytearray(data))

       # self._if.readline()

    def mbusRead(self,size):
        frame = b''

        while True:
            byte = self._if.read(size)
            frame += byte
            print(frame)
            if len(frame) == size:
                return frame

        return frame

    def SND_UD(self, body):
        _frame =[]
        _start = 0x68
        _stop = 0x16
        _size = len(body)
        _header =[_start, _size, _size, _start]
        print ('_header', _header)

        _frame = _header + body + [self._checksum(body)] + [_stop]
        print(_frame)

     #   print(bytearray(_frame))
        self.mbusWrite(_frame)

    def REQ_UD2(self, body):
        _frame = []
        _start = 0x10
        _stop = 0x16
        _size = len(body)
        _header = [_start]
        print('_header', _header)

#        _frame = [_start] + [0x40] + [0xff] + [0x3f] + [_stop]
 #       print(_frame)
  #      self.mbusWrite(_frame)

        _frame = _header + body + [self._checksum(body)] + [_stop]
        print(_frame)

        #   print(bytearray(_frame))
        self.mbusWrite(_frame)



    def addressChange(self,_old,_new):
        frame = []
        header =[0x68,0x06,0x06,0x68]
        body = [0x53,_old,0x51,0x01,0x7a,_new]
        stop = [0x16]
        x = 0
        for item in body:
            x = x + item
        print(x)
        checksum =  x % 256
        frame = header + body + [checksum] + stop
        print (frame)

        print(bytearray(frame))
        self.mbusWrite(frame)

        print (self.mbusRead(1))

    def setTimeDate(self):
        #type F 4Byte
        now = datetime.now()

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        y = datetime.now().year
        m = datetime.now().month
        d = datetime.now().day
        h = datetime.now().hour
        M = datetime.now().minute

        print(y, m, d, h, M)

        #minute
        int0 = M | 0x80

        #hour
        int1 = h | 0x80

        # highyear + month
        y = (y % 100) << 5
        highYear = ((y & 0xF00) >> 4)
        print(highYear,hex(highYear))
        int3 = highYear | m
        print(int3,hex(int3))

        #lowyear + day
        lowYear =  y & 0xff
        int2 = lowYear | d

        _body = [0x53, self._nodeId, 0x51, 0x04, 0x6d, int0, int1, int2, int3]

        self.SND_UD(_body)
        _timeout = time.time() + 5
        while time.time() < _timeout:
            _frame = self.mbusRead(1)
            if _frame[0] == 0xe5:
                print('OK')
                return True
            else:
                print('NOK')
                time.sleep(1)

        print('Timeout')
        return False

    def resetAppl(self):

        _body = [0x53, self._nodeId, 0x50]

        self.SND_UD(_body)
        _timeout = time.time() + 5
        while time.time() < _timeout:
            _frame = self.mbusRead(1)
            if _frame[0] == 0xe5:
                print('OK')
                return True
            else:
                print('NOK')
                time.sleep(1)

        return False

    def setConter(self):
        frame = []
        header = [0x68, 0x09, 0x09, 0x68]
        body = [0x53, 0x10, 0x51, 0x04, 0x13, 0x0, 0x0, 0x0, 0x0]
        stop = [0x16]

        x = 0
        for item in body:
            x = x + item
        print(x)
        checksum = x % 256
        frame = header + body + [checksum] + stop
        print(frame)
        print(bytearray(frame))
        self.mbusWrite(frame)

        print(self.mbusRead(1))

    def readValue(self):
        frame = []
        header = [0x10]
        body = [0x7b, 0x10]
        stop = [0x16]

        x = 0
        for item in body:
            x = x + item
        print(x)
        checksum = x % 256
        frame = header + body + [checksum] + stop
        print(frame)
        print(bytearray(frame))
        self.mbusWrite(frame)

        print(self.mbusRead(1))

    def readCounter(self):
        _body = [0x7b, self._nodeId]


        self.REQ_UD2(_body)
        _timeout = time.time() + 5
        #while time.time() < _timeout:
        _frame = self.mbusRead(4)
        print(_frame)
        size = _frame[1]
        print(size)
        _frame2 = self.mbusRead(size)
        y = 0
        n = ''
        print('type', type(_frame2))
        for x in _frame2:
            if y == 8:
                print(n)
                n = ' '
                y = 0

            y = y+ 1
          #  print(type(x))
           # n = "".join(["{:02x}".format(x).upper()])
            n = n + ',' + "".join('{:02x}'.format(x))
           # print(n)
        print(n)

       # print(_frame2)
        print('C Field', hex(_frame2[0]))
        print('Address', hex(_frame2[1]))
        print('CI Field', hex(_frame2[2]))
        print('Identificaiton Number', self._printNice(_frame[3:7]))
      #  print('Manufactur Code', hex(_frame[8:9]))

        return False





if __name__ == '__main__':
    mbus = serialIf()
    mbus.connect('/dev/ttyUSB1',2400)
    #mbus.setTimeDate()
   # mbus.addressChange(0x03,0x10)
   # mbus.dateChange()
   # mbus.setConter()
    #mbus.readValue()
   # mbus.resetAppl()
    mbus.readCounter()