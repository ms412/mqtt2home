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


__app__ = "serialS02mqtt Adapter"
__VERSION__ = "0.97"
__DATE__ = "17.02.2020"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2018 Markus Schiesser"
__license__ = 'GPL v3'

import os
import sys
import time
import serial
import json
import logging

from configobj import ConfigObj
from library.hw.sr04 import sr04
from library.logger import loghandler
from library.mqttclient import mqttclient


class manager(object):

    def __init__(self,configfile='ultrasonic2mqtt.cfg'):
        self._configfile = configfile

        self._general = None
        self._mqttbroker = None
        self._ultrasonic = None

        self._msg = {}

    def readConfig(self):
        _config = ConfigObj(self._configfile)

        if bool(_config) is False:
            print('ERROR config file not found',self._configfile)
            sys.exit()

        self._loggerCfg = _config.get('LOGGING',None)
        self._mqttCfg = _config.get('BROKER',None)
        self._interfaceCfg = _config.get('INTERFACE',None)
        return True

    def startLogger(self):
        self._root_logger = loghandler(self._loggerCfg.get('NAME','SERIAL2MQTT'))
        self._root_logger.handle(self._loggerCfg.get('LOGMODE','PRINT'),self._loggerCfg)
        self._root_logger.level(self._loggerCfg.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._loggerCfg.get('NAME', 'SERIAL2MQTT')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)
        return True

    def startMeasure(self):
        _result = {}
        for k1,v1 in self._interfaceCfg.items():
            print(k1,v1)
            port = v1.get('PORT','/dev/ttyUSB0')
            baudrate = v1.get('BAUDRATE',38400)
            port = serial.Serial(port, baudrate, timeout=3.0)
            self._log.debug('Serial Port configuration %s' % (port))
            port.flush()

            _temp = {}
            for k2,v2 in v1.items():
                if isinstance(v2,dict):

                    _data = {}
                    print('V2',k2,v2)
                    _offset = float(v2.get('OFFSET'))
                    _item = int(v2.get('BYTE'))
                    _factor = int(v2.get('FACTOR'))

                    number = port.write(b'$?\n')
                    time.sleep(1)
                    self._log.debug('Write %s bytes to Port %s' % (number, port.name))

                    _rcv = port.readline()
                    _str = _rcv.decode('ASCII')
                    _list = _str.split(';')

                    self._log.debug('Received data %s'%(_str))
                    _topic = k1 + '/' + k2
                    print('_topic',_topic,_list)
                    _value = float(_list[_item])/_factor

                    _data['S0']= _value + _offset
                    _data['S0_raw']  = _list[_item]

                    _temp[k2] = _data


                      #  self._msg[_topic]= _value + _offset
                       # self._msg[(_topic+'_raw')] = _list[_item]
        _result[k1] = _temp

        self._log.debug('Result %s' % (_result))

        return _result

    def publishData(self,data):
        self._log.debug('Methode: publishData(%s)',data)
        mqttpush = mqttclient(self._rootLoggerName)

        mqttpush.pushclient(self._mqttCfg)

        for k1, v1 in data.items():
            for k2,v2 in v1.items():
                print('send',k2,v2)
                _topic = self._mqttCfg.get('PUBLISH', '/SERIAL2MQTT')
                _topic = _topic + "/" + k1 + "/" + k2
                mqttpush.publish(_topic, json.dumps(v2))


        time.sleep(1)

        mqttpush.disconnect()
        return True

    def run(self):
        self.readConfig()
        self.startLogger()
        self._log.info('Startup, %s %s %s' % (__app__, __VERSION__, __DATE__))
      #  self._log.info('Start Reading Valuse')
        data = self.startMeasure()
        print('DAten',data)
        self._log.info(data)
        self.publishData(data)
        return True



if __name__ == '__main__':

    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile = './serialS02mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()
