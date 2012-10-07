class Block(object):
    """Class to define a block in a list"""
    start   = 0
    end     = 0
    value   = 0

    def __repr__(self):
        return str(self.value) + " ("+str(self.start)+","+str(self.end)+")"

    def _blockValue(self, valList):

        totalSum = 0
        for x in valList[self.start:self.end+1]:
            totalSum += x

        return totalSum

    def __init__(self, start, end, val=None, valList=None):
        self.start  = start
        self.end    = end
        if(val == None):
            self.value = self._blockValue(valList)
        else:
            self.value = val

class Separator(Block):
    """Class to define separators in a list"""
    def __init__(self, start, end, val, valList=None):
        self.separator = True
        super(separator, self).__init__(start, end, valList)