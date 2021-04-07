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


__app__ = "piface2mqtt Adapter"
__VERSION__ = "0.50"
__DATE__ = "07.04.2021"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2017 Markus Schiesser"
__license__ = 'GPL v3'

import os
import sys
import json
import time
import uuid
import logging
from configobj import ConfigObj

#from library.gpioFactory import gpioFactory
#from library.hw.dummyGpio import dummyGpio
from library.hw.pifaceGpio import pifaceGpio
from library.mqttclient import mqttclient
from library.logger import loghandler


class manager(object):
    def __init__(self,configfile):
       # self._log = loghandler('ONEWIRE')
        self._configfile = configfile

        self._logcfg = None
        self._mqttbroker = None

        self._gpioIF = None

        _watchdogID = uuid.uuid1()
        self._watchdogTopic = 'WATCHDOG/' + str(_watchdogID)

        self._watchdogTimer = time.time()

        self._ioStateUpdate = 30

    def readConfig(self):
        _config = ConfigObj(self._configfile)

        if bool(_config) is False:
            print('ERROR config file not found',self._configfile)
            sys.exit()

        self._cfglog = _config.get('LOGGING',None)
        self._brokerCfg = _config.get('BROKER',None)
        self._cfgPiFace = _config.get('PIFACE',None)
        return True

    def startLogger(self):
        self._root_logger = loghandler(self._cfglog.get('NAME','PIFACE2MQTT'))
        self._root_logger.handle(self._cfglog.get('LOGMODE','PRINT'),self._cfglog)
        self._root_logger.level(self._cfglog.get('LOGLEVEL','DEBUG'))
        self._rootLoggerName = self._cfglog.get('NAME', 'PIFACE2MQTT')
        self._log = logging.getLogger(self._rootLoggerName + '.' + self.__class__.__name__)
        return True

    def startMqtt(self):

        self._log.debug('Methode: startMqtt()')
        self._mqtt = mqttclient(self._rootLoggerName)

        _list = []

        _subscribe = (self._brokerCfg['SUBSCRIBE']) + '/#'
        _callback = self.brokerCallback

        _list.append({'SUBSCRIBE': _subscribe, 'CALLBACK': _callback})
        self._brokerCfg['SUBSCRIPTION'] = _list

        (state, message) = self._mqtt.fullclient(self._brokerCfg)
        if state:
            self._log.debug('mqtt completed with message %s', message)
        else:
            self._log.error('Failed to connect: %s', message)

        return False

    def startGpio(self):
        self._log.debug('Methode: startGpio with config %s', self._cfgPiFace)

        self._gpioIF = pifaceGpio()

        return True

    def brokerCallback(self,client,userdata,msg):
    #    print('callmeback1', client, userdata, msg)
        self._log.debug('mqttCallback: Topic ' + msg.topic + " QOS: " + str(msg.qos) + " Payload: " + str(msg.payload))
        _payload = {}
        _topic = msg.topic
        try:
            _payload = json.loads(msg.payload.decode())
            self.gpioWriteState({'TOPIC':msg.topic,'PAYLOAD':_payload})
        except:
            self._log.error('brockerCallback evalutation of Mqtt message failed: %s'% str(msg.payload))

       # self.gpioWriteState(_payload)
        return True

    def gpioWriteState(self,message = {}):
        self._log.debug('gpioWriteState called with %s'% message)

        _port = str((message['TOPIC']).split('/')[-1])
        _value = int(message['PAYLOAD'])
        self._log.debug('write to port: %d value: %d',int(self._cfgPiFace[_port]),_value)

        self._gpioIF.write(int(self._cfgPiFace[_port]),_value)

        return True

    def disconnectMqtt(self):
        self._log.debug('Methode:disconnectMqtt()')
        self._mqtt.disconnect()
        return True

    def callbackWatchog(self, client, userdata, message):
        self._log.debug('Methode: callbackWatchdog called with client: %s userdata: %s message: %s Topic: %s' % (client, userdata, message.payload, message.topic))

        self._watchdogTimer = time.time()

        return True

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
#        self.startSystem()
        self.readConfig()
        self.startLogger()

        self._log.info('Startup, %s %s %s'% ( __app__, __VERSION__, __DATE__) )
        self.startMqtt()
        self.startGpio()


        self.start_watchdog()
        time.sleep(2)
   #     self.disconnectMqtt()
        _timeout = time.time() + self._ioStateUpdate
        while True:
            time.sleep(1)
            if time.time() > _timeout:
                #    print('Send update')
            #    self.gpioReadState()
             #   self.publishData()
                self._log.debug('Timer expired update Watchdog')

                self._mqtt.publish(self._watchdogTopic, time.time())

                _timeout = time.time() + self._ioStateUpdate

            if time.time() > (self._watchdogTimer + 120):
                self._log.error('Watchdog timed out... restart system')
                sys.exit('kill my self')



if __name__ == '__main__':
    print('main')
    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile = '/opt/piface/piface2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()

