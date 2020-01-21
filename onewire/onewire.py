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
__VERSION__ = "0.95"
__DATE__ = "20.02.2018"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2017 Markus Schiesser"
__license__ = 'GPL v3'

import os
import sys
import time
from configobj import ConfigObj

from library.ds18b20 import ds18b20
from library.devicereader import devicereader
from library.mqttadapter import mqttadapter
from library.influx import influxWrapper
from library.loghandler import loghandler


class manager(object):
    def __init__(self,configfile='./onewire2mqtt.cfg'):
       # self._log = loghandler('ONEWIRE')
        self._configfile = configfile

        self._logcfg = None
        self._mqttbroker = None
        self._onewire = None


    def readConfig(self):
        #_cfg = configfile(self._configfile)
        #_config = _cfg.openfile()
        _config = ConfigObj(self._configfile)
        self._cfg_log = _config.get('LOGGING',None)
        self._cfg_mqtt = _config.get('BROKER',None)
        self._cfg_onewire = _config.get('ONEWIRE',None)
        self._cfg_influx = _config.get('INFLUX',None)
       # print(self._onewire)
        return True

    def startLogger(self):
        self._log = loghandler('ONEWIRE')
        self._log.handle(self._cfg_log.get('LOGMODE'),self._cfg_log)
        return True

    def startOneWire(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        return True

    def start_mqtt(self):
        self._log.debug('Methode: start_mqtt()')
        self._mqtt = mqttadapter(self._rootLoggerName)
        self._mqtt.connect(self._cfg_broker['HOST'])
        return True


    def readOneWire(self):
        result={}
        basedir = self._onewire.get('BASEDIR','/temp')
        devicefile = self._onewire.get('DEVICEFILE','w1_slave')
        deviceId = self._onewire.get('DEVICEID','28')
      #  print(basedir,devicefile,deviceId)

        ds = ds18b20()
        dr = devicereader(basedir,deviceId,devicefile)
        devices = dr.readdevice()
     #   print('devices found:', devices)
        for deviceId, deviceFile in devices.items():
         #   print(dr.readfile(deviceFile))
            data = dr.readfile(deviceFile)
            if data is not None:
                ds.readValue(data)
                result[deviceId]=ds.getCelsius()

        return result

    def publishData(self,data):
        for key,item in data.items():
            self._mqttclient.publish(key,item)
            _timeout = 0
            try:
                while not self._mqttclient.is_published():
                    time.sleep(2)
                    _timeout = _timeout + 1
                    if _timeout > 5:
                        raise TimeoutError
            except TimeoutError:
                self._log.error('Cannot publish Data - Timeout - %s %s '%(key,item))
                pass

        return True

    def writeInflux(self,data):
        if self._cfg_influx is not None:
            _host = self._cfg_influx.get('HOST','192.168.20.205')
            _port = self._cfg_influx.get('PORT',8086)
            _dbuser = self._cfg_influx.get('USER','testuser')
            _dbpasswd = self._cfg_influx.get('PASSWD','2Sec4You')
            _dbname = self._cfg_influx.get('DBNAME','testmeasure')
            _tags = self._cfg_influx.get('TAGS',{})

            influx = influxWrapper(self._rootLoggerName)
            influx.connectDB(_host,_port,_dbuser,_dbpasswd,_dbname)

            influx.createHaeder(_tags)
            influx.storeMeasurement(data)
            influx.writeMeasures()

            return True

        return False



    def stopMqttClient(self):
        self._log.debug('Disconnect from Mqtt Server')
        self._mqttclient.disconnect()
        return True


    def run(self):

        self.readConfig()
        self.startLogger()

        self._log.info('Startup, %s %s %s' % (__app__, __VERSION__, __DATE__))

        self.startOneWire()
        self.startMqttClient()
        data = self.readOneWire()
        self._log.info(data)
    #    self.publishData(data)
        self.publishData(data)
        self.writeInflux(data)
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