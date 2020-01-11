#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


__app__ = "onewire2mqtt Adapter"
__VERSION__ = "0.97"
__DATE__ = "21.12.2019"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2019 Markus Schiesser"
__license__ = 'GPL v3'

import os
import sys
import time
import logging
from configobj import ConfigObj

from library.ds18b20 import ds18b20
from library.devicereader import devicereader
from library.mqttclient import mqttclient
from library.logger import loghandler


class manager(object):
    def __init__(self,configfile='./onewire2mqtt.cfg'):
       # self._log = loghandler('ONEWIRE')
        self._configfile = configfile

        self._logcfg = None
        self._mqttbroker = None
        self._onewire = None

        self._rootLoggerName = ''


    def readConfig(self):
        _config = ConfigObj(self._configfile)

        if bool(_config) is False:
            print('ERROR config file not found',self._configfile)
            sys.exit()

        self._cfg_log = _config.get('LOGGING',None)
        self._cfg_mqtt = _config.get('BROKER',None)
        self._cfg_onewire = _config.get('ONEWIRE',None)
        return True

    def startLogger(self):

        self._root_logger = loghandler(self._cfg_log.get('NAME','ONEWIRE'))
        self._root_logger.handle(self._cfg_log.get('LOGMODE','PRINT'),self._cfg_log)
        self._root_logger.level(self._cfg_log.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._cfg_log.get('NAME', 'ONEWIRE')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)

        return True

    def startOneWire(self):
        self._log.debug('Methode: startOneWire()')
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        return True

    def startMqtt(self):
        self._log.debug('Methode: startMqtt()')

        self._mqtt = mqttclient(self._rootLoggerName)
        if self._mqtt.pushclient(self._cfg_mqtt):
            self._log.debug('Successfully connected to mqtt')
        else:
            self._log.error('Failed to connect to mqtt')
            exit()
        return True

    def readOneWire(self):
        self._log.debug('Methode: readOneWire()')
        result={}
        basedir = self._cfg_onewire.get('BASEDIR','/temp')
        devicefile = self._cfg_onewire.get('DEVICEFILE','w1_slave')
       # deviceId = self._cfg_onewire.get('DEVICEID','28')

        ds = ds18b20(self._rootLoggerName)
        dr = devicereader(basedir,devicefile,self._rootLoggerName)
        devices = dr.readDevice()
     #   print('devices found:', devices)
        for deviceId, deviceFile in devices.items():
            print(dr.readFile(deviceFile))
            data = dr.readFile(deviceFile)
            if data is not None:
                ds.readValue(data)
                result[deviceId]=ds.getCelsius()
        print(result)
        return result

    def publishData(self,data):
        self._log.debug('Methode: publishData(%s)',data)
        for key,item in data.items():
            self._mqtt.publish(key,item)

        return True

    def stopMqttClient(self):
        self._log.debug('Methode:stopMqttClient()')
        self._mqtt.disconnect()
        return True



    def run(self):

        self.readConfig()
        self.startLogger()

        self._log.info('Startup, %s %s %s' % (__app__, __VERSION__, __DATE__))

        self.startOneWire()
        self.startMqtt()
        data = self.readOneWire()
        self.publishData(data)
        time.sleep(5)
        self.stopMqttClient()
        return True


if __name__ == "__main__":

    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile = './onewire2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()
