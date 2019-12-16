
import os
import time
import logging
import paho.mqtt.client as mqtt

class mqttsimple():

    def __init__(self,config,logger):

        self._rootLogger = logger

        _libName = str(__name__.rsplit('.', 1)[-1])
        self._log = logging.getLogger(logger + '.' + _libName + '.' + self.__class__.__name__)
        #       print(logger + '.'+ _libName + '.' + self.__class__.__name__)

        self._log.debug('Create MQTT Wrapper Object')


        self._state = {'CONNECTED': False,
                       'SUBSCRIBED': False,
                       'PUBLISHED': 0}
    def construct(self):

        self._log.debug('Methode: construct ()')

        self._mqttc = mqtt.Client(str(os.getpid()), clean_session=True)

        self._mqttc.reconnect_delay_set(min_delay=10, max_delay=120)

        self._mqttc.enable_logger(logging.getLogger('mqttClient'))

        #   self._mqttc.enable_logger(self._rootLogger)

        self._mqttc.on_message = self.on_message
        self._mqttc.on_connect = self.on_connect
        self._mqttc.on_publish = self.on_publish
        self._mqttc.on_subscribe = self.on_subscribe
        self._mqttc.on_disconnect = self.on_disconnect
        #self._mqttc.on_log = self.on_log

        return True

    def connect(self, host, port=1883, keepalive=60, bind_address=""):

        self._log.debug('Methode: connect(%s, %d, %d)' % (host, port, keepalive))

        self._mqttc.connect_async(host, port, keepalive, bind_address)
        self._mqttc.loop_start()
   #     time.sleep(5)

    def on_connect(self, client, userdata, flags, rc):
        self._log.debug('Methode: on_connect(%s, %s, %s , %s'%(client,userdata,flags,rc))

        if rc == mqtt.CONNACK_ACCEPTED:
            self._log.info('MQTT connected')
            self._state['CONNECTED'] = True
        else:
            self._log.error('MQTT failed to connect: {}'.format(rc))
            self._state['CONNECTED']  = False
      #  print(self._state)
        return True

    def disconnect(self):
        self._log.debug('Methode: disconnect()')
     #   self._mqttc.wait_for_publish()
        self._state['CONNECTED'] = False
        self._mqttc.disconnect()
        return True

    def on_disconnect(self,client, userdata, rc):
        self._log.debug('Methode: on_dissconnect(%s, %s, %s)'%(client,userdata,rc))
        if rc != 0:
            self._log.error('Unexpected disconnection.')
        return True

    def subscribe(self, topic):
        self._log.debug('Methode: subscribe(%s)',topic)
        self._state['SUBSCRIBED'] = False

        while not self._state.get('CONNECTED'):
            self._log.debug('delay')
            time.sleep(0.3)

        (result, mid) = self._mqttc.subscribe(topic)

        if result == mqtt.MQTT_ERR_SUCCESS:
            while not self._state.get('SUBSCRIBED'):
                time.sleep(0.3)

            self._log.debug('MQTT subscribed to topic %s with success'% topic)
        else:
            self._log.error('MQTT failed to subscribe to topic %s'% topic)
            return False

        return True

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        self._log.debug('Methode: on_subscribe(%s, %s, %s, %s)'%(mqttc,obj,mid,granted_qos))
        self._state['SUBSCRIBED'] = True
        return True

    def publish(self,topic,payload):
        self._log.debug('Methode: publish(%s, %s)'%(topic,payload))
       # self._state['PUBLISHED'] = False
       # mid = False
       # rc = self._mqttc.publish(topic, payload)
       # print(rc)
       # try:
        (_result,_mid) = self._mqttc.publish(topic, payload)
       # rc.wait_for_publish()
        #result, mid = rc
#         print(self._state.get('PUBLISHED'), mid, result, rc)
       # print('RESSult:',(rc, mid, result))
        if _result == mqtt.MQTT_ERR_SUCCESS:
            self._log.debug("Message {} queued successfully.".format(_mid))
      #      self._state['PUBLISHED'] = mid
          #  print(self._state.get('PUBLISHED'), mid, result, rc)
            for _x in range(3):
#                print('xxx',self._state.get('PUBLISHED'), mid, result, rc)
               if self._state.get('PUBLISHED') == _mid:
                    self._log.debug('Message %d delivered', _mid)
                    return True
               else:
                    time.sleep(0.3)

            self._log.error('Message delivery timed out %d',_mid)

        else:
            self._log.error("Failed to publish message. Error: {}".format(_result))
           #     print('Faile')
        #except Exception as e:
         #   self._log.error("EXCEPTION RAISED: {}".format(e))

        return False

    def on_publish(self, client, userdata, mid):
      #  print('TEST',mid)
        self._log.debug('Methode: on_publish(%s, %s, %s)'%(client,userdata,mid))
        self._state['PUBLISHED'] = mid
        return True

    def on_message(self, client, userdata, message):
        self._log.debug('Methode: on_message(%s, %s, %s)'%(client,userdata,message))
    #    print("Received message '" + str(message.payload) + "' on topic '"
     #         + message.topic + "' with QoS " + str(message.qos))
        self._log.debug('Received message Topic: {}'.format(message.topic))
        return message

    def message_callback_add(self, topic, callback):
        self._log.debug('Methode: message_callback_add(%s, %s'%(topic,callback))
        self._mqttc.message_callback_add(topic, callback)
    #    print('callbvac',x)
     #   self._log.debug('Registerd Callback Topic: {}'.format(topic))
        return True


class callmeback(object):

    def callback(self,client, userdata, msg):
        print('callmeback',client, userdata, msg)
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('simpleExample')
    config1 = {'HOST': '192.168.1.107', 'PUBLISH': '/TEST', 'SUBSCRIBE': '/TEST/', 'CONFIG': '/TEST2/'}


    callme = callmeback()
    mqttc = mqttsimple(config1,'simpleExample')
    mqttc.construct()
    mqttc.connect('192.168.20.205')
    mqttc.subscribe('/TEST11/#')
    mqttc.message_callback_add('/TEST11/#',callme.callback)
    time.sleep(5)
    mqttc.publish('/TEST11/zz',u'122')
    mqttc.publish('/TEST11/zz', u'133')
    mqttc.publish('/TEST12/zz', u'144')
    mqttc.publish('/TEST11/zz',u'122')
    mqttc.publish('/TEST12/zz', u'133')
    mqttc.publish('/TEST12/zz', u'144')
    #time.sleep(5)
    mqttc.disconnect()
    time.sleep(5)