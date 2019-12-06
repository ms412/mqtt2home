


class BinaryOut(object):
    def __init__(self,config):
        print('Binary Out')
        self._io = config.get('GPIO',None)
        self._attenuation = config.get('ATTENUATIN','UP')

    def setup(self):
        print('setup')

    def set(self,value):
        print('set',value)

    def get(self):
        print('get')

