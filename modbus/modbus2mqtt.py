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


__app__ = "Modbus2mqtt Adapter"
__VERSION__ = "0.95"
__DATE__ = "03.02.2020"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2017 Markus Schiesser"
__license__ = 'GPL v3'

import os
import sys
import json
import logging
from configobj import ConfigObj

from library.modbus import modbus
from library.mqttclient import mqttclient
from library.logger import loghandler


class manager(object):
    def __init__(self,configfile):
       # self._log = loghandler('ONEWIRE')
        self._configfile = configfile

        self._logcfg = None
        self._mqttbroker = None
        self._modbus = {}
        self._commands = None

    def readConfig(self):
        _config = ConfigObj(self._configfile)

        if bool(_config) is False:
            print('ERROR config file not found',self._configfile)
            sys.exit()

        self._cfglog = _config.get('LOGGING',None)
        self._cfgMqtt = _config.get('BROKER',None)
        self._cfgModbus = _config.get('MODBUS',None)
        return True

    def startLogger(self):
        self._root_logger = loghandler(self._cfglog.get('NAME','MODBUS'))
        self._root_logger.handle(self._cfglog.get('LOGMODE','PRINT'),self._cfglog)
        self._root_logger.level(self._cfglog.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._cfglog.get('NAME', 'ONEWIRE')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)
        return True

    def startMqtt(self):
        self._log.debug('Methode: startMqtt()')

        self._mqtt = mqttclient(self._rootLoggerName)
        if self._mqtt.pushclient(self._cfgMqtt):
            self._log.debug('Successfully connected to mqtt')
        else:
            self._log.error('Failed to connect to mqtt')
            exit()
        return True

    def modbus(self):
        _modbusConfig = {}
        _modbusConfig['INTERFACE'] = self._cfgModbus.get('INTERFACE','/dev/ttyUSB0')
        _modbusConfig['BAUDRATE'] = self._cfgModbus.get('BAUDRATE',9800)
    #    self._modbus = modbus(_modbusConfig,self._rootLoggerName)
     #   self._modbus.setup()
        print('xx',type(self._cfgModbus),self._cfgModbus)

        for key, value in self._cfgModbus.items():
            print(key)

            if type(value) is not str:
                _modbusConfig['DEVICEID'] = key
                self._modbus = modbus(_modbusConfig, self._rootLoggerName)
                self._modbus.setup()
                print('yy',value)

                _result = {}
                for call, args in value.items():
                    print('data',call, args)
             #   value =0
                    data = self._modbus.read(args)
               # value  = 0
                    if data is not None:
                        _result[call]= data

                    print('Result',key,_result,call)

                self.publishData(key,_result)
       # print(result)
        return True


    def publishData(self,devicename,data):
        self._log.debug('Methode: publishData(%s,%s)'%(devicename,data))
        _publish = self._cfgMqtt.get('PUBLISH','/MODBUS') + '/' + devicename

        self._mqtt.publish(_publish,json.dumps(data))
        return True

    def disconnectMqtt(self):
        self._log.debug('Methode:disconnectMqtt()')
        self._mqtt.disconnect()
        return True

    def run(self):
#        self.startSystem()
        self.readConfig()
        self.startLogger()

        self._log.info('Startup, %s %s %s'% ( __app__, __VERSION__, __DATE__) )
        self.startMqtt()
        self.modbus()
        self.disconnectMqtt()



if __name__ == '__main__':
    print('main')
    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile ='./modbus2mqtt.cfg'
     #   configfile = 'modbus2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()

