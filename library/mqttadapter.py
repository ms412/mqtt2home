

import os
import time
import logging
#from interruptingcow import timeout
import paho.mqtt.client as mqtt
from queue import Queue


#.class_logger = logging.getLogger('marantec.mqttadapter')

class mqttadapter():

    def __init__(self,logger):

        _libName = str(__name__.rsplit('.',1)[-1])
        self._log = logging.getLogger(logger + '.'+ _libName + '.' + self.__class__.__name__)
 #       print(logger + '.'+ _libName + '.' + self.__class__.__name__)

        self._log.debug('Create MQTT Adapter Object')

        self._broker = mqttc(logger)

    def connect(self, host, port=1883):

   #     print('Connect')
        self._broker.connect(host,port)

        _timeout = time.time()+10
        _try = 5
        while  _timeout > time.time():
        #    print('timeloop')
            time.sleep(1)
            if self._broker.state()['CONNECTED'] == True:
                self._log.info = ('MQTT client connected to %s',host)
             #   print('connected')
                return True
            else:
                if _try:
                 #   time.sleep(1)
                    _try = _try -1
                    self._log.debug('MQTT failed to connect try again %d', _try)
                else:
                    self._log.error('Failed to connect after %d tries', _try)
                    self._log.error('MQTT failed to connect to host %s' % host)
                    return False

        self._log.error('Timeout: Failed to connect to MQTT broker')
        return False

    def subscribe(self, topic, callback):

        self._broker.subscribe(topic)

        _timeout = time.time() + 5
        while _timeout > time.time():
            time.sleep(1)
            if self._broker.state()['SUBSCRIBED'] == True:
                self._log.info = ('MQTT Subscribed with success to topic %s',topic)
           #     print('subscribed')
                self._broker.message_callback_add(topic, callback)
                return True
            else:
                self._log.error('MQTT could not subscribe try agian')

        self._log.error('Timeout to subscribe')
        return False

    def publish_old(self, topic, message):

        self._broker.publish(topic, message)

        _timeout = time.time() + 5
        while _timeout > time.time():
            time.sleep(1)
            if self._broker.state()['PUBLISHED'] == True:
                self._log.info = ('MQTT Published to topic %s', topic)
                return True
            else:
                self._log.error('Could not deliver message, try again')

        self._log.error('Failed to deliver message')
        return False

    def publish_zz(self,topic,message):
        mid = self._broker.publish(topic, message)

        if mid:
            _timeout = time.time() + 5
            while _timeout > time.time():
                if self._broker.state()['PUBLISHED'] == mid:
                    self._log.info = ('MQTT Published to topic %s', topic)
                    return True
                else:
                    time.sleep(0.5)

        else:
            self._log('Cannot Publish message %s to topic: %s'%(message,topic))

            return True

    def publish(self,topic,message):
        self._broker.publish(topic, message)




class mqttc(object):

    def __init__(self, logger):

        _libName = str(__name__.rsplit('.',1)[-1])
        self._log = logging.getLogger(logger + '.'+ _libName + '.' + self.__class__.__name__)

        self._log.debug('Create MQTT Client start')

        self._mqttc = mqtt.Client(str(os.getpid()), clean_session=True)

        self._mqttc.on_message = self.on_message
        self._mqttc.on_connect = self.on_connect
        self._mqttc.on_publish = self.on_publish
        self._mqttc.on_subscribe = self.on_subscribe
        self._mqttc.on_disconnect = self.on_disconnect
     #   self._mqttc.on_log = self.on_log
     #   self._log = class_logger

        self._state = {'CONNECTED': False,
                       'SUBSCRIBED': False,
                       'PUBLISHED': False}

    def state(self):
        return self._state

    def connect(self,host, port=1883, keepalive=60, bind_address=""):
        self._log.debug('Connecting to host: {}'.format(host))
        self._mqttc.connect_async(host, port, keepalive, bind_address)
        self._mqttc.loop_start()
        return True

    def on_connect(self, client, userdata, flags, rc):
        if rc == mqtt.CONNACK_ACCEPTED:
            self._log.info('MQTT connected')
            self._state['CONNECTED'] = True
        else:
            self._log.error('MQTT failed to connect: {}'.format(rc))
            self._state['CONNECTED'] = False
      #  print(self._state)
        return True

    def disconnect(self):
        self._log.debug('Disconnect from MQTT')
        self._mqttc.disconnect()
        return True

    def on_disconnect(self, client, userdata, rc):
        if rc == mqtt.MQTT_ERR_SUCCESS:
            self._log.info('MQTT disconnected')
            self._state ['CONNECTED'] = False
        else:
            self._log.error('MQTT dissconected with Error: {}'.format(rc))
            self._state['CONNECTED'] = False

        return True

    def subscribe(self, topic, hostname="mqtt.eclipse.org", retained=False, msg_count=2   ):
        self._state['SUBSCRIBED'] = False

        (result, mid) = self._mqttc.subscribe(topic)
    #    print('subscribe', result, mid)

        if result == mqtt.MQTT_ERR_SUCCESS:
            self._log.debug('MQTT subscribed to topic %s with success'% topic)
        else:
            self._log.error('MQTT failed to subscribe to topic %s'% topic)
            return False

        return True

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        #print("Subscribed: " + str(mid) + " " + str(granted_qos))
        self._log.debug('Subscribed successfully')
        self._state['SUBSCRIBED'] = True

        return True

    def publish(self,topic,payload):
        self._state['PUBLISHED'] = False
        mid = False
        try:
            rc = self._mqttc.publish(topic, payload)
            result, mid = rc
           # print('RESSult:',(rc, mid, result))
            if result == mqtt.MQTT_ERR_SUCCESS:
                self._log.debug("Message {} queued successfully.".format(mid))
            #    print('success')
            else:
                self._log.error("Failed to publish message. Error: {}".format(result))
           #     print('Faile')
        except Exception as e:
            self._log.error("EXCEPTION RAISED: {}".format(e))

        return mid

    def on_publish(self, client, userdata, mid):
        #print('Published')
        #print("mid: " + str(mid), userdata)
        self._log.debug("Message {} publisehed.".format(mid))
        self._state['PUBLISHED'] = mid
        return True

    def on_message(self, client, userdata, message):
    #    print("Received message '" + str(message.payload) + "' on topic '"
     #         + message.topic + "' with QoS " + str(message.qos))
        self._log.debug('Received message Topic: {}'.format(message.topic))
        return message

    def message_callback_add(self, topic, callback):
        self._mqttc.message_callback_add(topic, callback)
    #    print('callbvac',x)
        self._log.debug('Registerd Callback Topic: {}'.format(topic))
        return True

    def unsubscribe(self,channel):
       # print('mqtt unsubscribe')
        self._mqttc.unsubscribe(self._subscribe)
        return True



if __name__ == "__main__":

    def function1(client, userdata, message):
        print ('function',client,'userdata', userdata,'message',message)
        print(str(message.payload))
        print(str(message.topic))
        print(str(message.qos))
        _topic = message.topic
        _t = _topic.split('/')
        x = _t[-2]
        y = _t[-1]
        print(_t,x,y)

    config1 = {'HOST':'192.168.20.205','PUBLISH':'/TEST','SUBSCRIBE':'/TEST/','CONFIG':'/TEST2/'}
    config2 = {'HOST':'localhost','PUBLISH':'/TEST','SUBSCRIBE':['/TEST1/#','/TEST3','/TEST4']}
    msg = {'CHANNEL':'/TEST/CONFIG','MESSAGE':'{ioioookko}'}
    broker = mqttc()
  #  broker = setup(config)
 #   broker.start()

#    broker.connect('192.168.20.205',1883)
    broker.connect('127.0.0.1', 1883)
    time.sleep(5)



    broker.subscribe('CH/GRAGEDOOR/#')
    time.sleep(5)
    broker.publish('/TEST/','TEST')
    broker.message_callback_add('CH/GRAGEDOOR/#',function1)
    time.sleep(10)
   # broker.restart(config1)
 #   time.sleep(10)

    while True:
        time.sleep(1)
        #broker.publish(msg)
   # time.sleep(2)