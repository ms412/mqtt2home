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


__app__ = "mbus2mqtt Adapter"
__VERSION__ = "0.70"
__DATE__ = "10.05.2020"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2020 Markus Schiesser"
__license__ = 'GPL v3'

import sys
import serial
import json
import logging
import meterbus

from configobj import ConfigObj
from library.logger import loghandler
from library.mqttclient import mqttclient


class manager(object):

    def __init__(self,configfile='mbus2mqtt.cfg'):
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
        self._root_logger = loghandler(self._loggerCfg.get('NAME','MBUS2MQTT'))
        self._root_logger.handle(self._loggerCfg.get('LOGMODE','PRINT'),self._loggerCfg)
        self._root_logger.level(self._loggerCfg.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._loggerCfg.get('NAME', 'MBUS2MQTT')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)
        return True

    def startMbus(self):
        _device = self._interfaceCfg.get('PORT', '/dev/ttyUSB0')
        _baudrate = self._interfaceCfg.get('BAUDRATE', 2400)

        self._if = serial.Serial(_device, _baudrate, 8, 'E', 1, 0.5)
        self._log.debug('Serial Port configuration %s' % (_device))
        self._if.flush()

    def readMbus(self):

        _data = {}
        for k,v in self._interfaceCfg.items():
          if isinstance(v, dict):
            _slaveId = k
            _offset = v.get('OFFSET',0)

            meterbus.send_ping_frame(self._if, _slaveId)
            frame = meterbus.load(meterbus.recv_frame(ser, 1))
            assert isinstance(frame, meterbus.TelegramACK)
            meterbus.send_request_frame(self._if, _slaveId)
            frame = meterbus.load(meterbus.recv_frame(self._if, meterbus.FRAME_DATA_LENGTH))
            assert isinstance(frame, meterbus.TelegramLong)
            _data = json.loads(frame.to_JSON())

            _payload = {}
            _payload['WATER_CONSUMPTION'] = (x['body']['records'][0]['value'])
            print(_payload)
            _data[_slaveId] = _payload

        return(_data)

    def publishData(self,data):
        self._log.debug('Methode: publishData(%s)',data)
        mqttpush = mqttclient(self._rootLoggerName)

        mqttpush.pushclient(self._mqttCfg)

        for k, v in data.items():
              print('send',k,v)
              _topic = self._mqttCfg.get('PUBLISH', 'SMARTHOME/CH/BE/SENSOR01/MBUS01')
              _topic = _topic + "/" + k
              mqttpush.publish(_topic, json.dumps(v))

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
        configfile = './mbus2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()



import os, time, serial, meterbus
import json
import paho.mqtt.publish as publish
