

import sys
import time
import threading
import logging

from library.hwIf_raspberry  import raspberry
#from library.hwIf_dummy import raspberry

class marantec250c(threading.Thread):

    def __init__(self,config,threadId,callback,logger):
        threading.Thread.__init__(self)

        _libName = str(__name__.rsplit('.',1)[-1])
        self._log = logging.getLogger(logger + '.'+ _libName + '.' + self.__class__.__name__)
      #  print(self._log)
      #  time.sleep(3)
        self._log.debug('Start instance of marantec250c object')
       # print(_libName)
       # print(logger)

        self._config = config
        self._threadId = threadId
        self._callback = callback
      #  self._hwHandle = dummy(logger)
        self._hwHandle = raspberry(logger)

        self._id = config

        self._gpio_closed = 0
        self._gpio_opened = 0
        self._gpio_up = 0
        self._gpio_down = 0
        self._gpio_ledGreen = 0
        self._gpio_ledRed = 0

        # UP/DOWN/MOWING
  #      self._gateState = None
        #LOCK/UNLOCK
 #       self._stateLock = None
        #ON/OFF
#        self._stateLight = None

        self._garageDoorState= {'DOOR':None,
                                 'LOCK': None,
                                 'LIGHT': None}

    def startup(self):

        self._log.debug('Methode: startup()')
        # config gate state
        self._gpio_closed = int(self._config['CLOSED'])
        self._gpio_opened = int(self._config['OPENED'])
        self._gpio_up = int(self._config['UP'])
        self._gpio_down = int(self._config['DOWN'])
        self._gpio_locked = int(self._config['LOCK'])
        self._gpio_light = int(self._config['LIGHT'])
        self._gpio_ledGreen = int(self._config['LED_GREEN'])
        self._gpio_ledRed = int(self._config['LED_RED'])

   #     print(self._gpio_closed,self._gpio_opened,self._gpio_up,self._gpio_down,self._gpio_ledGreen,self._gpio_ledRed)

        self._hwHandle.ConfigIO(self._gpio_closed,'IN','UP')
        self._hwHandle.ConfigIO(self._gpio_opened, 'IN', 'UP')
        self._hwHandle.Interrupt(self._gpio_closed, self.callbackWrapper,'BOTH')
        self._hwHandle.Interrupt(self._gpio_opened, self.callbackWrapper,'BOTH')
    #    self._hwHandle.start()
        self._hwHandle.ConfigIO(self._gpio_up, 'OUT')
        self._hwHandle.ConfigIO(self._gpio_down,'OUT')
        self._hwHandle.ConfigIO(self._gpio_locked, 'OUT')
        self._hwHandle.ConfigIO(self._gpio_light, 'OUT')
        self._hwHandle.ConfigIO(self._gpio_ledGreen, 'OUT')
        self._hwHandle.ConfigIO(self._gpio_ledRed, 'OUT')

        self._hwHandle.WritePin(self._gpio_up,0)
        self._hwHandle.WritePin(self._gpio_down,0)
        self._hwHandle.WritePin(self._gpio_locked, 0)
        self._hwHandle.WritePin(self._gpio_light, 0)

        self.updateGarageDoorState()

    def callbackWrapper(self, channel):
        self._log.debug('Methode: callbackWrappe(Channel %s'%channel)
        time.sleep(2)
        self.updateGarageDoorState()
        return True

    def updateGarageDoorState(self):
        self._log.debug('Methode: updateGarageDoorState()')
     #   _tempState = self._garageDoorState
        _tempState = {}
        #print('Test Garage Door State ',self._hwHandle.ReadPin(self._gpio_closed),self._hwHandle.ReadPin(self._gpio_opened))
        if (not (self._hwHandle.ReadPin(self._gpio_closed))) & (not (self._hwHandle.ReadPin(self._gpio_opened))):
            _tempState['DOOR'] = 'MOVING'
            self.setLed('YELLOW')
            self._log.info('Garagedoor Moving')
        elif (not (self._hwHandle.ReadPin(self._gpio_closed))) & self._hwHandle.ReadPin(self._gpio_opened):
            _tempState['DOOR'] = 'OPEN'
            self.setLed('GREEN')
            self._log.info('Garagedoor Open')
        elif self._hwHandle.ReadPin(self._gpio_closed) & (not (self._hwHandle.ReadPin(self._gpio_opened))):
            _tempState['DOOR'] ='CLOSE'
            self.setLed('RED')
            self._log.info('Garagedoor Closed')
        else:
            self._log.error('Unknown State')

        if self._hwHandle.ReadPin(self._gpio_light):
            _tempState['LIGHT'] = 'ON'
            self._log.info('Light on')
        else:
            _tempState['LIGHT'] = 'OFF'
            self._log.info('Light off')

        if self._hwHandle.ReadPin(self._gpio_locked ):
            _tempState['LOCK'] = 'LOCKED'
            self._log.info('Garagedoor Locked')
        else:
            _tempState['LOCK'] = 'UNLOCKED'
            self._log.info('Garagedoor Unlocked')

    #    print ('DOOR',self._garageDoorState)
     #   print('TEMP', _tempState)
        if self._garageDoorState != _tempState:
            #print ('cahnge')
            self._log.debug('Garagdoor changed from %s to %s', self._garageDoorState, _tempState)
            self._garageDoorState = _tempState
            self._callback(self._threadId)

        return True

    def getGarageDoorState(self):
        self._log.debug('Methode: getGarageDoorState()')
  #      self.changeGaragDoorState()

        json_body = [
            {
            "time": time.time(),
            "fields": {
                "DOOR" : self._garageDoorState.get('DOOR',None),
                "LIGHT" : self._garageDoorState.get('LIGHT',None),
                "LOCK" : self._garageDoorState.get('LOCK',None)
                }
            }
        ]

        self._log.debug('getGarageDoorState Message: {}'.format(json_body))

        return json_body
            #json.dumps(json_body)

    def setLed(self,color):
        self._log.debug('Methode: setLed(color: %s)'% color)

        if 'YELLOW' in color:
            self._hwHandle.WritePin(self._gpio_ledRed,1)
            self._hwHandle.WritePin(self._gpio_ledGreen, 1)
        elif 'RED' in color:
            self._hwHandle.WritePin(self._gpio_ledRed, 1)
            self._hwHandle.WritePin(self._gpio_ledGreen, 0)
        elif 'GREEN' in color:
            self._hwHandle.WritePin(self._gpio_ledRed, 0)
            self._hwHandle.WritePin(self._gpio_ledGreen, 1)
        else:
            self._log.error('LED color not defined Color: {}'.format(color))
        return True


    def setGarageDoorState(self, type, state):
        self._log.debug('Methode: setGarageDoorState(type: %s state: %s)' %(type,state))
        if 'DOOR' == type:
          #  print('DOOR :', state)
          #  self._garageDoorState['DOOR'] = state
          #  print('1',self._hwHandle.ReadPin(self._gpio_up), self._hwHandle.ReadPin(self._gpio_down))
           # print('11',self._hwHandle.ReadPin(self._gpio_closed),self._hwHandle.ReadPin(self._gpio_opened))
            if 'OPEN' in state:
                self._hwHandle.WritePin(self._gpio_up, 1)
              #  print('2', self._hwHandle.ReadPin(self._gpio_up), self._hwHandle.ReadPin(self._gpio_down))
               # print('21', self._hwHandle.ReadPin(self._gpio_closed), self._hwHandle.ReadPin(self._gpio_opened))
                time.sleep(0.75)
               # print('22', self._hwHandle.ReadPin(self._gpio_closed), self._hwHandle.ReadPin(self._gpio_opened))
                self._hwHandle.WritePin(self._gpio_up, 0)
               # print('3', self._hwHandle.ReadPin(self._gpio_up), self._hwHandle.ReadPin(self._gpio_down))
               # print('31', self._hwHandle.ReadPin(self._gpio_closed), self._hwHandle.ReadPin(self._gpio_opened))
            #    self._garageDoorState['DOOR'] = 'OPEN'
                self._log.debug('Door UP')
            else:
                self._hwHandle.WritePin(self._gpio_down, 1)
                time.sleep(0.75)
                self._hwHandle.WritePin(self._gpio_down, 0)
             #   self._garageDoorState['DOOR'] = 'CLOSE'
                self._log.debug('Door DOWN')

        elif 'LOCK' == type:
            #print('LOCK', state)
         #   self._garageDoorState['LOCK'] = state
            if 'LOCK' == state:
                self._hwHandle.WritePin(self._gpio_locked,1)
              #  self._garageDoorState['LOCK'] = 'LOCKED'
                self._log.debug('switch LOCK on')
            else:
                self._hwHandle.WritePin(self._gpio_locked,0)
               # self._garageDoorState['LOCK'] = 'UNLOCKED'
                self._log.debug('switch LOCK off')

        elif 'LIGHT' == type:
           # print('LIGHT', state)
          #  self._garageDoorState['LIGHT']=state
            if 'ON' in state:
                self._hwHandle.WritePin(self._gpio_light,1)
               # self._garageDoorState['LIGHT'] = 'ON'
                self._log.debug('switch LIGHT on')
            else:
                self._hwHandle.WritePin(self._gpio_light,0)
                #self._garageDoorState['LIGHT'] = 'OFF'
                self._log.debug('switch LIGHT off')
        self.updateGarageDoorState()
        return

