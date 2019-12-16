

import os
import time
import logging
import threading
import paho.mqtt.client as mqtt
from queue import Queue


class mqttwrapper(threading.Thread):

    def __init__(self,config,logger):
        threading.Thread.__init__(self)

        print(logger)
        self._rootLogger = logger

        _libName = str(__name__.rsplit('.', 1)[-1])
        print(_libName)
        self._log = logging.getLogger(logger + '.' + _libName + '.' + self.__class__.__name__)
        #       print(logger + '.'+ _libName + '.' + self.__class__.__name__)

        self._log.debug('Create MQTT Wrapper Object')

        self._stateConnection = False

    def construct(self):

        self._log.debug('Methode: construct ()')

        self._mqttc = mqtt.Client(str(os.getpid()), clean_session=True)

        self._mqttc.reconnect_delay_set(min_delay=10, max_delay=120)
        self._mqttc.enable_logger(self._rootLogger)

        self._mqttc.on_message = self.on_message
        self._mqttc.on_connect = self.on_connect
        self._mqttc.on_publish = self.on_publish
        self._mqttc.on_subscribe = self.on_subscribe
        self._mqttc.on_disconnect = self.on_disconnect

        return True

    def connect(self,host, port=1883, keepalive=60, bind_address=""):

        self._log.debug('Methode: connect(%s, %d, %d)'%(host,port,keepalive))

        _retry = 5

        for _try in range(_retry):
            self._mqttc.connect_async(host, port, keepalive, bind_address)
            time.sleep(3)

            if self._stateConnection:
                self._log.info = ('MQTT client connected to %s', host)
                self._mqttc.loop_start()
                return True
            else:
                self._log.info('MQTT failed to connect, try again %d',_try)
                time.sleep(10)

        self.log.error('Failed to connect to %s',host)
        return False

    def on_connect(self, client, userdata, flags, rc):
        self._log.debug('Methode: on_connect(%s, %s, %s , %s'%(client,userdata,flags,rc))

        if rc == mqtt.CONNACK_ACCEPTED:
            self._log.info('MQTT connected')
            self._stateConnection = True
        else:
            self._log.error('MQTT failed to connect: {}'.format(rc))
            self._stateConnection = False
      #  print(self._state)
        return True

    def run(self):


        print('run thread')
        self.construct()
        self.connect('192.168.20.205')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('simpleExample')
    config1 = {'HOST': '192.168.1.107', 'PUBLISH': '/TEST', 'SUBSCRIBE': '/TEST/', 'CONFIG': '/TEST2/'}


    mqttc = mqttwrapper(config1,'simpleExample')
    mqttc.start()
