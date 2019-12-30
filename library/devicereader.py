import os
import logging
import re
import glob

class devicereader(object):
    def __init__(self,basedir,devicefile,logger):

        _libName = str(__name__.rsplit('.', 1)[-1])
        self._log = logging.getLogger(logger + '.' + _libName + '.' + self.__class__.__name__)

        self._log.debug('Create Devicereader Object')

        self._basedir =os.path.join('c:', os.sep, basedir)
       # self._deviceid = deviceid
        self._devicefile = devicefile
       # print('basedir', self._basedir)

    def readDevice(self):
        self._log.debug('Methode:readDevice()')
        result = {}
      #  print(os.listdir(self._basedir))
        for name in os.listdir(self._basedir):
            pathname = os.path.join(os.sep, self._basedir, name)
            if os.path.isdir(pathname):
            #    temp = os.path.join(self._basedir + '/' + self._deviceid)
                deviceId = os.path.basename(os.path.normpath(pathname))
                device_file = os.path.join(os.sep, pathname, self._devicefile)
                result[deviceId]=device_file
        return result

    def readFile(self, filename):
        self._log.debug('Methode: readFile(%s)',filename)
        try:
            with open(filename)as fh:
                lines = fh.readlines()
                fh.close()
        except:
            lines = None
            self._log.error('failed open file: %s',filename)

        return lines

