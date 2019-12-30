
import os
import time
import logging
import paho.mqtt.client as mqtt


class mqttclient(object):

    def __init__(self,logger):

        _libName = str(__name__.rsplit('.', 1)[-1])
        self._log = logging.getLogger(logger + '.' + _libName + '.' + self.__class__.__name__)

        self._log.debug('Create MQTT mqttclient Object')

        self._host =''
        self._port = 1883
        self._subscribe = {}

        self._state = {'CONNECTED': False,
                       'SUBSCRIBED': False,
                       'PUBLISHED': 0}

    def __del__(self):
        print('delte')
       # self._log.debug('Delete MQTT mqttclient Object')

    def construct(self):
        self._log.debug('Methode: construct ()')

        self._mqttc = mqtt.Client(str(os.getpid()), clean_session=False)
        self._mqttc.reconnect_delay_set(min_delay=5, max_delay=60)
        self._mqttc.enable_logger(logging.getLogger('mqttClient'))

        self._mqttc.on_message = self.on_message
        self._mqttc.on_connect = self.on_connect
        self._mqttc.on_publish = self.on_publish
        self._mqttc.on_subscribe = self.on_subscribe
        self._mqttc.on_disconnect = self.on_disconnect
        return True

    def connect(self, host, port=1883, keepalive=60, bind_address=""):
        self._log.debug('Methode: connect(%s, %d, %d)' % (host, port, keepalive))
        self._state['CONNECTED'] = False

        self._mqttc.connect_async(host, port, keepalive, bind_address)
        self._mqttc.loop_start()

        for _x in range(30):
     #       print('1')
            if self._state.get('CONNECTED',False):
       #         print('conn')
                self._log.debug('Connected to host %s', host)
         #       self._mqttc.loop_start()
                return True
            else:
                time.sleep(0.3)

        return False

    def on_connect(self, client, userdata, flags, rc):
        self._log.debug('Methode: on_connect(%s, %s, %s , %s' % (client, userdata, flags, rc))

        if rc == mqtt.CONNACK_ACCEPTED:
            self._log.info('MQTT connected')
            self._state['CONNECTED'] = True
        else:
            self._log.error('MQTT failed to connect: {}'.format(rc))
            self._state['CONNECTED'] = False

        return True

    def disconnect(self):
        self._log.debug('Methode: disconnect()')
        #   self._mqttc.wait_for_publish()
        self._state['CONNECTED'] = False
        self._mqttc.disconnect()
        return True

    def on_disconnect(self, client, userdata, rc):
        self._log.debug('Methode: on_dissconnect(%s, %s, %s)' % (client, userdata, rc))
        if rc != 0:
            self._log.error('Unexpected disconnection.')

        return True

    def subscribe(self, topic):
        self._log.debug('Methode: subscribe(%s)', topic)

        (_result, _mid) = self._mqttc.subscribe(topic)

        if _result == mqtt.MQTT_ERR_SUCCESS:
            self._log.debug('MQTT subscribed to topic %s with success' % topic)
        else:
            self._log.error('MQTT failed to subscribe to topic %s' % topic)
            return False

        return True

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        self._log.debug('Methode: on_subscribe(%s, %s, %s, %s)' % (mqttc, obj, mid, granted_qos))
        return True

    def publish(self, topic, payload):
        self._log.debug('Methode: publish(%s, %s)' % (topic, payload))

        (_result, _mid) = self._mqttc.publish(topic, payload)

        if _result == mqtt.MQTT_ERR_SUCCESS:
            self._log.debug("Message {} queued successfully.".format(_mid))

            for _x in range(3):
                if self._state.get('PUBLISHED') == _mid:
                    self._log.debug('Message %d delivered', _mid)
                    return _mid
                else:
                    time.sleep(0.3)
        else:
            self._log.error("Failed to publish message. Error: {}".format(_result))

        return False

    def on_publish(self, client, userdata, mid):
        self._log.debug('Methode: on_publish(%s, %s, %s)' % (client, userdata, mid))
        self._state['PUBLISHED'] =mid
        return True

    def on_message(self, client, userdata, message):
        self._log.debug('Methode: on_message(%s, %s, %s)' % (client, userdata, message))
        #    print("Received message '" + str(message.payload) + "' on topic '"
        #         + message.topic + "' with QoS " + str(message.qos))
        self._log.debug('Received message Topic: {}'.format(message.topic))
        return message

    def callback(self, topic, callback):
        self._log.debug('Methode: message_callback_add(%s, %s' % (topic, callback))
        self._mqttc.message_callback_add(topic, callback)
        #    print('callbvac',x)
        #   self._log.debug('Registerd Callback Topic: {}'.format(topic))
        return True

    def pushclient(self,config):
        self._log.debug('Methode: pushclient(%s)',config)

        self._host = str(config.get('HOST','localhost'))
        self._port = int(config.get('PORT',1883))
        self.construct()

        return self.connect(self._host,self._port)

    def fullclient(self,config):
        self._log.debug('Methode: fullclient(%s)',config)

        self._host = str(config.get('HOST','localhost'))
        self._port = int(config.get('PORT',1883))
        self._subscribtion = config.get('SUBSCRIPTION',None)
        _result = False

        self.construct()
        if self.connect(self._host,self._port):


            if self._subscribtion is not None:
              #  print('hier')
                for item in self._subscribtion:
                  #  print(item)
                    _topic = item.get('SUBSCRIBE')
                    _callback = item.get('CALLBACK',None)
                    if self.subscribe(_topic):
                        if _callback is not None:
                            self.callback(_topic,_callback)
                    else:
                        return (False,'Subscription Failed')
        else:
            return (False,'Not Connected')

        return (True,'Connected')

class callmeback(object):

    def callback1(self, client, userdata, msg):
        print('callmeback1', client, userdata, msg)
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    def callback2(self, client, userdata, msg):
        print('callmeback2', client, userdata, msg)
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('mqttclient')
    config1 = {'HOST': '192.168.20.205', 'CONFIG': '/TEST2/'}

    callme = callmeback()
    mqttpush = mqttclient('simpleExample')
    print(mqttpush.pushclient(config1))
    print(mqttpush.publish('/TEST/PUSH','1234567'))
    mqttpush.disconnect()

    time.sleep(10)

    mqttfull = mqttclient('fullExample')

    z={}
    w={}
    y=[]
    z['SUBSCRIBE']='/TEST/FULL/2'
    z['CALLBACK']=callme.callback2
    w['SUBSCRIBE']='/TEST/FULL/1'
    w['CALLBACK']=callme.callback1
    y.append(z)
    y.append(w)
    config1['SUBSCRIPTION']=y
    print(config1)

    (state,message) = mqttfull.fullclient(config1)
    print(state,message)
    while True:
        time.sleep(5)
       # print(mqttfull.publish('/TEST/FULL/1', '12312412341235'))
        if mqttfull.publish('/TEST/FULL/1','12312412341235') is not False:
            print('TRUE')
         #   time.sleep(3)
        else:
            print('FALSE')
         #   time.sleep(3)

