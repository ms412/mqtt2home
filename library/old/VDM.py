

import sys
import time
import threading
import logging
from library.vpm import BinaryOut

logger = logging.getLogger(__name__)


class vdm(threading.Thread):

    def __init__(self, config,callback):
        threading.Thread.__init__(self)

        self._config = config
        self._callback = callback
        self._hwHandle = {}

    def setup(self):

        for key, item in self._config.items():
            if 'BINARY-OUT' in item.get('MODE'):
                self._hwHandle[key] = BinaryOut(item)
                self._hwHandle.get(key).setup()
            if 'BINARY-IN'in item.get('MODE'):
                self._hwHandle[key] = BinaryOut(item)
                self._hwHandle.get(key).setup()

