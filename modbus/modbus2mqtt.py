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
import logging
from configobj import ConfigObj

from library.mqttpush import mqttpush
from library.modbus import modbus
from library.mqttclient import mqttclient
from library.logger import loghandler
from library.influx import influxWrapper


class manager(object):
    def __init__(self,configfile):
       # self._log = loghandler('ONEWIRE')
        self._configfile = configfile

        self._logcfg = None
        self._mqttbroker = None
        self._modbus = None
        self._commands = None

    def readConfig(self):
        _config = ConfigObj(self._configfile)

        if bool(_config) is False:
            print('ERROR config file not found',self._configfile)
            sys.exit()

        self._cfglog = _config.get('LOGGING',None)
        self._cfgMqtt = _config.get('BROKER',None)
        self._cfgModbus = _config.get('MODBUS',None)
        self._cfgDevice = _config.get('DEVICE',None)
        self._cfgInflux = _config.get('INFLUX',None)
        return True

    def startLogger(self):
        self._root_logger = loghandler(self._cfg_log.get('NAME','ONEWIRE'))
        self._root_logger.handle(self._cfg_log.get('LOGMODE','PRINT'),self._cfg_log)
        self._root_logger.level(self._cfg_log.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._cfg_log.get('NAME', 'ONEWIRE')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)
        return True

    def connectInfluxDB(self):
        self._log.debug('Methode: connectInfluxDB()')
        _host = self._cfgInflux.get('HOST','localhsot')
        _port = self._cfgInflux.get('PORT',8086)
        _dbuser = self._cfgInflux.get('DBUSER','default')
        _dbpasswd = self._cfgInflux.get('DBPASSWD','Geheim')
        _dbname = self._cfgInflux.get('DBNAME','measurement')

        self._influx = influxWrapper(self._rootLoggerName)
        self._influx.connectDB(_host,_port,_dbuser,_dbpasswd,_dbname)
        self._influx.createHaeder(self._cfgInflux.get('HEADER'))
        return True

    def modbus(self):
      #  result = {}
        for devicename,item in self._commands.items():
           # print(key,item['CONFIG']['MODBUSID'])
            print(devicename,item)
            self._modbus['DEVICEID']=item['CONFIG']['MODBUSID']
            self._mgr = modbus(self._modbus,self._log)
            self._mgr.setup()
            _channel = item.get('PUBLISH','/OPENAHB/AC')
            self._influx.addTag('ID',item.get('MODBUSID'))
            print(item)
            _result = {}
            for key,item in item['CALLS'].items():
                print('data',key, item)
             #   value =0
                value = self._mgr.read(item)
               # value  = 0
                if value is not None:
                    _result[key]= value

            print('Result',_result,devicename)
            self.publishData(devicename,_result)
       # print(result)
        return True

    def publishData(self,channel,data):
        mqttc = mqttpush(self._mqttbroker)
        main_channel = self._mqttbroker.get('PUBLISH','/OPENHAB')

        for item, measurement in data.items():
            _channel = main_channel + '/' + channel + '/' + item
            self._log.debug('channel: %s, mesage %s'% (_channel,measurement))
            mqttc.publish(_channel,measurement)

        return True

    def run(self):
#        self.startSystem()
        self.readConfig()
        self.startLogger()

        self._log.info('Startup, %s %s %s'% ( __app__, __VERSION__, __DATE__) )
        self.modbus()
       # self.publishData(data)



if __name__ == '__main__':
    print('main')
    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile ='/opt/Modbus2mqtt/modbus2mqtt.cfg'
     #   configfile = 'modbus2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()

