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


__app__ = "ultrasonic2mqtt Adapter"
__VERSION__ = "0.92"
__DATE__ = "17.02.2020"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2017 Markus Schiesser"
__license__ = 'GPL v3'


import os
import sys
import time
import json
import logging

from configobj import ConfigObj
from library.hw.sr04 import sr04
from library.logger import loghandler
from library.mqttclient import mqttclient



class manager(object):

    def __init__(self,configfile):
        self._configfile = configfile

        self._general = None
        self._mqttbroker = None
        self._ultrasonic = None

    def readConfig(self):
        _config = ConfigObj(self._configfile)

        if bool(_config) is False:
            print('ERROR config file not found',self._configfile)
            sys.exit()

        self._loggerCfg = _config.get('LOGGING',None)
        self._mqttCfg = _config.get('BROKER',None)
        self._ultrasonicCfg = _config.get('ULTRASONIC',None)
        return True

    def startLogger(self):
        self._root_logger = loghandler(self._loggerCfg.get('NAME','ONEWIRE'))
        self._root_logger.handle(self._loggerCfg.get('LOGMODE','PRINT'),self._loggerCfg)
        self._root_logger.level(self._loggerCfg.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._loggerCfg.get('NAME', 'ONEWIRE')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)
        return True

    def measure(self):
        result = {}
        for item, value in self._ultrasonicCfg.items():
            value = {}
            _trigger = value.get('TRIGGER',24)
            _echo = value.get('ECHO',23)
            us = sr04(_trigger,_echo)
            value['LEVEL'] = us.measure_average()
            result[item]=value
            del us
           # result[item] = 5

        return result

    def publishData(self,data):
        self._log.debug('Methode: publishData(%s)',data)
        mqttpush = mqttclient(self._rootLoggerName)

        mqttpush.pushclient(self._mqttCfg)

        for key, value in data.items():
            _topic = self._mqttCfg.get('PUBLISH', '/ULTRASONIC')
            _topic = _topic + "/" + key
            mqttpush.publish(_topic, json.dumps(value))


        time.sleep(1)

        mqttpush.disconnect()
        return True

    def run(self):
        self.readConfig()
        self.startLogger()

        self._log.info('Startup, %s %s %s' % (__app__, __VERSION__, __DATE__))

        data = self.measure()
        self.publishData(data)
        return True

if __name__ == "__main__":

    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile = './ultrasonic2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()
