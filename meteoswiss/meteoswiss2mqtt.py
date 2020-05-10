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


__app__ = "Meteoswiss2mqtt Adapter"
__VERSION__ = "0.6"
__DATE__ = "16.03.2020"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2029 Markus Schiesser"
__license__ = 'GPL v3'

import os
import sys
import json
import time
import logging
import meteoswiss
from configobj import ConfigObj

from library.mqttclient import mqttclient
from library.logger import loghandler


class manager(object):
    def __init__(self,configfile):
       # self._log = loghandler('ONEWIRE')
        self._configfile = configfile

        self._logcfg = None
        self._mqttbroker = None
        self._ms = None
        self._stationId = None

    def readConfig(self):
        _config = ConfigObj(self._configfile)

        if bool(_config) is False:
            print('ERROR config file not found',self._configfile)
            sys.exit()

        self._cfglog = _config.get('LOGGING',None)
        self._cfgMqtt = _config.get('BROKER',None)
        self._cfgMeteoSwiss = _config.get('METEOSWISS',None)
        return True

    def startLogger(self):
        self._root_logger = loghandler(self._cfglog.get('NAME','METEOSWISS2MQTT'))
        self._root_logger.handle(self._cfglog.get('LOGMODE','PRINT'),self._cfglog)
        self._root_logger.level(self._cfglog.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._cfglog.get('NAME', 'METEOSWISS2MQTT')
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

    def getStation(self,plz):
        self._ms = meteoswiss.meteoswiss()
        self._stationId = self._ms.getStationByAreaCode(plz)[0]

    def getTemperature(self):
        return self._ms.temperatureCurrent(self._stationId)[1]

    def getRainfall(self):
        return self._ms.rainCurrent(self._stationId)[1]

    def getPressure(self):
        return self._ms.pressureCurrent(self._stationId)['qfe']

    def getSunshine(self):
        return self._ms.sunCurrent(self._stationId)[1]

    def getWindspeed(self):
        return self._ms.windCurrent(self._stationId)[1]

    def getHumidity(self):
        return self._ms.humidityCurrent(self._stationId)[1]

    def collectMeasurements(self):
        result = {"MeteoSwiss-Temperature" : self.getTemperature(),
                  "MeteoSwiss-Rainfall" : self.getRainfall(),
                  "MeteoSwiss-Pressure": self.getPressure(),
                  "MeteoSwiss-Sunshine" : self.getSunshine(),
                  "MeteoSwiss-Windspeed" : self.getWindspeed(),
                  "MeteoSwiss-Humidity" : self.getHumidity()}
        print('Result',result)
        return(result)

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

#        while(True):
        self.startMqtt()
       # print(self._cfgMeteoSwiss.get('STATION',3053))
        self.getStation(self._cfgMeteoSwiss.get('STATION',3053))
        data = self.collectMeasurements()
        self.publishData(self._cfgMeteoSwiss.get('STATION',3053),data)
        self.disconnectMqtt()




if __name__ == '__main__':
    print('main')
    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile ='./meteoswiss2mqtt.cfg'


    mgr_handle = manager(configfile)
    mgr_handle.run()

