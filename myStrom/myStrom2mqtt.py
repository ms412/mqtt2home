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


__app__ = "myStrom2mqtt Adapter"
__VERSION__ = "0.50"
__DATE__ = "02.03.2020"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2020 Markus Schiesser"
__license__ = 'GPL v3'

import os
import sys
import time
import uuid
import json
import logging
from configobj import ConfigObj

from library.mqttclient import mqttclient
from library.logger import loghandler
from library.hw.myStrom import myStrom


class manager(object):
    def __init__(self,configfile):
       # self._log = loghandler('ONEWIRE')
        self._configfile = configfile

        self._deviceStore = {}

        _watchdogID = uuid.uuid1()
        self._watchdogTopic = 'WATCHDOG/' + str(_watchdogID)


    def readConfig(self):
        _config = ConfigObj(self._configfile)

        if bool(_config) is False:
            print('ERROR config file not found',self._configfile)
            sys.exit()

        self._loggerCfg = _config.get('LOGGING',None)
        self._brokerCfg = _config.get('BROKER',None)
        self._devices = _config.get('MYSTROM',None)
        return True

    def startLogger(self):
        self._root_logger = loghandler(self._loggerCfg.get('NAME','INFLUX2MQTT'))
        self._root_logger.handle(self._loggerCfg.get('LOGMODE','PRINT'),self._loggerCfg)
        self._root_logger.level(self._loggerCfg.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._loggerCfg.get('NAME', 'INFLUX2MQTT')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)
        return True

    def startmyStromDevices(self):
        self._log.debug('Methode: startmyStromDevices(config %s)', self._devices)
        for k,v in self._devices.items():
            #print(k,v)
            self._deviceStore[k] = myStrom(v,k,self.callbackDevice,self._rootLoggerName)
            self._deviceStore[k].start()
            #print(k, v,self._deviceStore[k])
        #print('complete')

    def getmyStromState(self):
        self._log.debug('Methode: getmyStromState()')

        result = {}
        for k,v in self._devices.items():
            result[k] = self._deviceStore[k].getState()
          #  print(result,k, v )
        return result

    def callbackDevice(self,id):
        self._log.debug('Methode: callbackDevices(DeviceID: %s)', id)
        _instance = self._deviceStore[id]
        #print(_instance)
        _payload = _instance.getState()
        self.startMqttClient()
        self.publishMqtt(id,_payload)
        self.stopMqttClient()
        return True

    def startMqttClient(self):
        self._log.debug('Methode: startMqttClient()')
        self._mqttpush = mqttclient(self._rootLoggerName)
        self._mqttpush.pushclient(self._brokerCfg)
        #print('START')

    def publishMqtt(self,topic,payload):
        self._log.debug('Methode: pubishMqtt(topci %s, payload %s)'% (topic,payload))
        #print(topic,payload)
        _topic = self._brokerCfg.get('PUBLISH','SMARTHOME/CH/BE/OPENVPN/MYSTROM')+'/'+topic
        self._mqttpush.publish(_topic, json.dumps(payload))
 #       print('publish')

    def stopMqttClient(self):
        self._log.debug('Methode: stopMqttClient')
#        print('dissconnect')
        self._mqttpush.disconnect()
        return True



    def run(self):
        """
        Entry point, initiates components and loops forever...
        """
        self.readConfig()
        self.startLogger()
        time.sleep(2)

        self._log.info('Startup, %s %s %s' % (__app__, __VERSION__, __DATE__))
       # self.start_mqtt()
       # self.start_watchdog()
        self.startmyStromDevices()
       # time.sleep(2)
        while(True):
            time.sleep(20)
       #     print('TIMEOUT')
            self.startMqttClient()
            result = self.getmyStromState()
        #    print(result,type(result))
            for k,v in result.items():
         #       print('Publish', k,v)
                self.publishMqtt(k,v)

            self.stopMqttClient()



if __name__ == '__main__':

    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile ='./myStrom2mqtt.cfg'
     #   configfile = 'gpio2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()

