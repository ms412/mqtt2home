
import os
import re
import time
import logging

class ds18b20(object):
    def __init__(self,logger):
        _libName = str(__name__.rsplit('.',1)[-1])
        self._log = logging.getLogger(logger + '.'+ _libName + '.' + self.__class__.__name__)

        self._log.debug('Create Instance of Class: ds18b20')

        self._temperature = 0

    def readValue(self, lines):
        self._log.debug('Methode: readValue(%s)',lines)
        result = False
      #  print(lines)

        for x in range (3):
            if lines[0].strip()[-3:] != 'YES':
                #print('error')
                self._log.error('Conversion of data failed')
                time.sleep(0.2)
            else:
                equals_pos = lines[1].find('t=')
                if equals_pos != -1:
                    temp_string = lines[1][equals_pos + 2:]
                    self._temperature = float(temp_string) / 1000.0
                    reslut = True
            self._log.error('No Data')
        return result

    def getCelsius(self):
        return self._temperature

    def getFahreinheit(self):
        return self._temperature *9.0 / 5.0 +32