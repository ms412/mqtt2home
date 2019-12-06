
class bitoperation(object):
    '''
    Bit Operation class
    '''
    def __init__(self):
        '''
        create object
        '''

    def setBit(self,int_type,offset):
        '''
        setBit
        int_type    bit field
        offset      number of bit to be manipulated
        return      modified bit field
        '''
        mask = 1 << offset
        return(int_type | mask)

    def testBit(self,int_type,offset):
        '''
        testBit
        int_type    bit field
        offset      number of bit to be manipulated
        return      modified bit field
        '''
        mask = 1 << offset
        return(int_type & mask)

    def clearBit(self,int_type,offset):
        '''
        clearBit
        int_type    bit field
        offset      number of bit to be manipulated
        return      modified bit field
        '''
        mask = ~(1 << offset)
        return(int_type & mask)

    def toggleBit(self,int_type,offset):
        '''
        toggleBit
        int_type    bit field
        offset      number of bit to be manipulated
        return      modified bit field
        '''
        mask = 1 << offset
        return(int_type ^ mask)