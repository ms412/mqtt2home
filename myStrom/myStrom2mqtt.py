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
            print(k,v)
            self._deviceStore[k] = myStrom(v,k,self.callbackDevice)
            self._deviceStore[k].start()
            print(k, v,self._deviceStore[k])

    def getmyStromState(self):

        for k,v in self._devices.items():
            result = self._deviceStore[k].getState()
            print(result,k, v )

        return (v,result)

    def callbackDevice(self,id):
        self._log.debug('Methode: callbackDevices(DeviceID: %s)', id)
        _instance = self._deviceStore[id]
        print(_instance)



    def callbackBroker(self,client, userdata, message):
        # topic /CH/GARAGEDOOR/ID{0/1}/FUNCTION{OPEN/CLOSE/LOCK/LIGHT
        # topic /SMARTHOME/CH/BE/SENSOR01CH/ONEWIRE01/TEMPERATURE
        # SMARTHOME = database
        #CH = Tag (COUNTRY)
        #BE = Tag (LOCATION)
        #Node = Tag(Node)
        #ONEWIRE = TAG (BUS)
        #TEMPERATURE = TAG (MEASUREMENT)
        self._log.debug('Methode: callbackBroker called with client: %s userdata: %s message: %s Topic: %s'%(client, userdata, message.payload, message.topic))
        _marantecObj = ''
        _topic = message.topic
        _payload = message.payload.decode()

        _t = _topic.split('/')
        _dbname = _t[0]
        _tag = {}
      #  print(self._cfgInflux.get('TAG'))
        for index, item in enumerate(self._cfgInflux.get('TAG'), start=1):
     #       print(item,index,_tag)
            _tag[item] = _t[index]

        self._log.debug('Create Influx Tag: %s',_tag)
     #   print(type(_payload))
      #  print(type(json.loads(_payload)))
       # print(json.loads(_payload))

        self.connectInfluxDB(_dbname)
        self._influx.createHaeder(_tag)
        self._influx.storeMeasurement(json.loads(_payload))
        self._influx.writeMeasures()

        return True

    def callbackWatchog(self, client, userdata, message):
        self._log.debug('Methode: callbackWatchdog called with client: %s userdata: %s message: %s Topic: %s' % (client, userdata, message.payload, message.topic))

        self._watchdogTimer = time.time()

        return True





    def start_mqtt(self):
        self._log.debug('Methode: start_mqtt()')
        self._mqtt = mqttclient(self._rootLoggerName)

        _list = []

     #   _subscribe = (self._cfg_broker['PUBLISH']) + '/#'
      #  _callback = self.callbackWatchog

       # _list.append({'SUBSCRIBE': _subscribe, 'CALLBACK': _callback})

        _subscribe = (self._brokerCfg['SUBSCRIBE'])+'/#'
        _callback = self.callbackBroker

        _list.append({'SUBSCRIBE': _subscribe, 'CALLBACK': _callback})
        self._brokerCfg['SUBSCRIPTION'] = _list

        (state, message) = self._mqtt.fullclient(self._brokerCfg)
        if state:
            self._log.debug('mqtt completed with message %s',message)
        else:
            self._log.error('Failed to connect: %s',message)

        return False

    def start_watchdog(self):
        self._log.debug('Methode: start_mqttWatchdog()')

        _callback = self.callbackWatchog
        if self._mqtt.subscribe(self._watchdogTopic):
            if _callback is not None:
                self._mqtt.callback(self._watchdogTopic, _callback)
        else:
            self._log.error('Failed to setup Watchdog')
            return False

        self._watchdogTimer = time.time()
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
        time.sleep(2)
        while(True):
            time.sleep(10)
            self.getmyStromState()



if __name__ == '__main__':

    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile ='./myStrom2mqtt.cfg'
     #   configfile = 'modbus2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()

