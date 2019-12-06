
import sys
import time
import threading
import logging

from library.hwIf_raspberry  import raspberry
from library.hwIf_dummy import dummy

logger = logging.getLogger(__name__)


class gpioManager(threading.Thread):

    def __init__(self, config, callback):
        threading.Thread.__init__(self)

        self._cfg = config
        self._callback = callback

    def setup(self):

        for _pin, _cfg in self._cfg.items():
        #    print(_pin, _cfg)
            if isinstance(_cfg, dict):

                if 'RASPBERRY' in _cfg.get('HWIF', 'RASPBERRY'):
                    self._hwHandle = raspberry(self._log)
                elif 'DUMMY' in _cfg.get('HWIF', 'RASPBERRY'):
                    self._hwHandle = dummy(self._log)
                else:
                    self._log.critical('HWInterface %s unknown' % _cfg.get('HWIF', None))
                    sys.exit()

                #self._devHandle[_pin] = S0(self._hwHandle, _pin, _cfg, self._log)
                self._devHandle[_pin] = S0Gas(self._hwHandle, _cfg)

        return True