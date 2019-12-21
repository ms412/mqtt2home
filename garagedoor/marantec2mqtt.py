#!/usr/bin/python3
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


__app__ = "Marantec Adapter"
__VERSION__ = "0.8"
__DATE__ = "18.12.2019"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2019 Markus Schiesser"
__license__ = 'GPL v3'

import os
import sys
import time
import json
import logging
import threading

from configobj import ConfigObj
from library.hwadapter import marantec250c
from library.mqttclient import mqttclient
from library.logger import loghandler
#from library.S0Manager import S0manager

class manager(threading.Thread):

    def __init__(self,cfg_file='marantec2mqtt.cfg'):
        threading.Thread.__init__(self)

        self._cfg_file = cfg_file

        self._cfg_broker = None
        self._cfg_log = None
        self._cfg_gpio = None

        self._rootLoggerName = ''


    def read_config(self):

        _cfg = ConfigObj(self._cfg_file)

        if bool(_cfg) is False:
            print('ERROR config file not found',self._cfg_file)
            sys.exit()
            #exit

        self._cfg_broker = _cfg.get('BROKER',None)
        self._cfg_log = _cfg.get('LOGGING',None)
        self._cfg_gpio = _cfg.get('GATES',None)
      #  self._cfg_msgAdapter = _cfg.get('BROKER',None)
        return True

    def start_logger(self):
       # self._log = loghandler('marantec')
        self._root_logger = loghandler(self._cfg_log.get('NAME','Marantec'))
        self._root_logger.handle(self._cfg_log.get('LOGMODE','PRINT'),self._cfg_log)
        self._root_logger.level(self._cfg_log.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._cfg_log.get('NAME','Marantec')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)
        return True

    def callbackDevice(self,threadId):
        self._log.debug('Methode: callbackDevice with value ThreadID %s'%(threadId))
       # print('callback',threadId)
        #print(self._marantecObj[threadId].getGarageDoorState())

        _topic = self._cfg_broker['PUBLISH'] + '/' + threadId + '/STATE'
        self._mqtt.publish(_topic, json.dumps(self._marantecObj[threadId].getGarageDoorState()))

        return True

    def callbackBroker(self,client, userdata, message):
        # topic /CH/GARAGEDOOR/ID{0/1}/FUNCTION{OPEN/CLOSE/LOCK/LIGHT
        self._log.debug('Methode: callbackBroker called with client: %s userdata: %s message: %s Topic: %s'%(client, userdata, message.payload, message.topic))
        _marantecObj = ''
        _topic = message.topic
        _payload = message.payload.decode()

        _t = _topic.split('/')
        _objectId = _t[-2]
        _functionId = _t[-1]
      #  print(self._marantecObj, _objectId )
        _marantecObj = self._marantecObj[_objectId]
        _marantecObj.setGarageDoorState(_functionId, _payload)

        return True

    def start_marantec(self):
        self._log.debug('Methode: start_marantec()')
        self._marantecObj = {}

        self._log.debug('Start GPIO Interface with configuration: %s'% (self._cfg_gpio))
        for k,i in self._cfg_gpio.items():
            self._marantecObj[k]=marantec250c(self._cfg_gpio[k],k,self.callbackDevice,self._rootLoggerName)

        for k,i in self._marantecObj.items():
            i.startup()

        return True

    def start_mqtt(self):
        self._log.debug('Methode: start_mqtt()')
        self._mqtt = mqttclient(self._rootLoggerName)

        _list = []

        _subscribe = (self._cfg_broker['SUBSCRIBE'])+'/#'
        _callback = self.callbackBroker

        _list.append({'SUBSCRIBE': _subscribe, 'CALLBACK': _callback})
        self._cfg_broker['SUBSCRIPTION'] = _list

        (state, message) = self._mqtt.fullclient(self._cfg_broker)
        if state:
            self._log.debug('mqtt completed with message %s',message)
        else:
            self._log.error('Failed to connect: %s',message)

        return False



    def run(self):
        """
        Entry point, initiates components and loops forever...
        """
        self.read_config()
        self.start_logger()
        time.sleep(2)

        self._log.info('Startup, %s %s %s'% ( __app__, __VERSION__, __DATE__) )
        self.start_mqtt()
        time.sleep(2)
        self.start_marantec()
        _timeout = time.time()+30
        while True:
            time.sleep(10)
            if time.time() > _timeout:
            #    print('Send update')
                self._log.debug('Timer expired get update')

                for k, i in  self._marantecObj.items():
                    i.updateGarageDoorState()
                    self.callbackDevice(k)

                _timeout = time.time() + 30



if __name__ == "__main__":

    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile = 'C:/Users/markus/PycharmProjects/mqtt@home/garagedoor/marantec2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.start()