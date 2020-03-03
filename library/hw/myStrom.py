
import time
import requests
import threading


class myStrom(threading.Thread):

    def __init__(self, ip,id, callback):
        threading.Thread.__init__(self)

        self._handle = myStromSwitch(ip)

        self._ip = ip
        self._id = id
        self._callback = callback

        self._temperature = 0.0
        self._power = 0.0
        self._state = None
        self._startup = True

        self._t0 = 0.0

        self._polling = 10

    def update(self):
      #  print('test',type( self._handle.consumption()))
        if self._handle.get_status():
            if self._startup:
                self._t0 = time.time()
                self._power = self._handle.consumption()
                self._temperature = self._handle.temperature()
                self._startup = False
            else:
                self._power = (self._power + self._handle.consumption()) /2
                self._temperature = (self._temperature + self._handle.temperature()) /2
        #    print(self._power,self._temperature)



     #   print('ff',self._state, self._handle.relay())
        if self._state != self._handle.relay():
            self._state = self._handle.relay()
            self._callback(self._id)
       #     print(self._switch)

    def getState(self):
        _t1 = time.time() - self._t0
     #   print('T',self._t0, _t1, self._power)
        _energy = self._power * _t1 /3600/1000
        _data =  ({'myStrom_Power': self._power, 'myStrom_Energy' :_energy, 'myStrom_Temperature': self._temperature, 'myStrom_Switch': self._state})
        self._startup = True
        return _data


    def run(self):
        while True:
  #          print('update')
            time.sleep(self._polling)
            self.update()

class myStromSwitch(object):

    def __init__(self,host):

        self._host = host
        self._uri = 'http://' + host

        self._consumption = 0.0
        self._temperature = 0.0
        self._relay = None

    def get_status(self):

        _state  = False

        try:
            response = requests.get(self._uri + '/report', timeout=5)
          #  print('result',response.text, response.status_code)
           # msg = 'Get Status' + str(self._url) + str(r.json())
            #self._log.debug(msg)
            if response.status_code == 200:
                _response= response.json()
              #  print(str(_response))
                _state = True
                self._consumption = float(_response["power"])
                self._relay = str(_response["relay"])
                try:
                    self._temperature = float(_response["temperature"])
                except KeyError:
                    self._temperature = 0
            else:
           #     print('failed to get valid data')
                _state = 'UNEXPECTED RESPONSE'


        except requests.Timeout:
            msg = 'TIMEOUT' + str(self._uri)
            _state = 'TIMEOUT'
     #       print('TIMEOUT',msg)
        except requests.exceptions.ConnectionError:
            msg = 'CONNECTION Error' + str(self._uri)
            _state = 'CONNECTION ERROR'
     #       print('CONNECTION Error',msg)
        #    print('state',_state)
        return (_state)

    def relay(self):
        return self._relay

    def consumption(self):
        return self._consumption

    def temperature(self):
        return self._temperature









