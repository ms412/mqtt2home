
import datetime
from datetime import datetime

class longFrame(object):

    def __init__(self):

        self._start = 0x68
        self._stop = 0x16
        self._L = 0x00
        self._C = 0x00
        self._A = 0x00
        self._CI = 0x00

    def setField(self,L,C,A,CI):
        self._L = L
        self._C = C
        self._A = A
        self._CI = CI


    def convert(self):


        # datetime object containing current date and time
        now = datetime.now()

        print("now =", now)

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        y = datetime.now().year
        m = datetime.now().month
        d = datetime.now().day
        h = datetime.now().hour
        M = datetime.now().minute


        print(y,m,d,h,M)

        min = M | 0x80
        print('Min',min, hex(min),hex(M))
        hour = h & 0x08
        print('hour',hour, (hex(hour)))
        day = d & 0x1F
        print('day', hex(day))
        mon = m
        print('Month',hex(mon))

        num1 = y//100
        num2 = y %100
        print(num1, num2)

        decimal_string = str(y)

        digits = [int(c) for c in decimal_string]
        print(digits)

        digits = [20,16]
        zero_padded_BCD_digits = [format(d,'04b') for d in digits]
        print(zero_padded_BCD_digits)
        x = zero_padded_BCD_digits[0]
        print(type(x),x)
        xx = int(x)
        yy = xx & 0xE0
        print(hex(yy))


    def markus(self):
        now = datetime.now()

        print("now =", now)

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        y = datetime.now().year
        m = datetime.now().month
        d = datetime.now().day
        h = datetime.now().hour
        M = datetime.now().minute


        print(y,m,d,h,M)

        min = M | 0x80
        print('min, U16', min, hex(min),hex(M))
        print('int1', hex(min))

        hour = h | 0x80
        print('hour',hour, (hex(hour)))
        day = d & 0x1F
        print('day', hex(day))
        print('int2',hex(hour))

        y = 2020
        hh = y %100
      #  h = 20
        print(type(hh),bin(hh))
        hh = hh << 5
        #
        print('year',bin(hh))
        highYear = ((hh & 0xF00) >> 4)
        print('highYear',hex(highYear))
        int4 = highYear | m
        print('int4',hex(int4))

        lowYear = (hh & 0xff)
        int3 = lowYear | d
        print('int3', hex(int3))

    def bytTest(self):
        data = b''
        y = bytes([0xe5])
        print('y',type(y),y)
        x = bytearray(y)
        print(type(x), type(x[0]))
        data += x
        print(data)
        if x[0] == 0xe5:
            print('t')

        else:
            print('gg')




if __name__ == '__main__':
    x = longFrame()
  #  x.convert()
    #x.markus()
    x.bytTest()