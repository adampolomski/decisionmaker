'''
Created on 25 sty 2015

@author: Adam Polomski
'''

import math

class ProbabilisticModel(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''        

    @staticmethod
    def valueFrequency(values, rolls):
        '''
        '''
        length = len(values)
        frequencies = {}
        lastValue = values[0]
        
        for i in range(0, length):  
            curEvent = length - i  
            eventCount = math.pow(curEvent, rolls) - math.pow(curEvent - 1, rolls)
            oldFrequency = frequencies.pop(values[i], 0)
            frequencies.setdefault(values[i], eventCount + oldFrequency)
            
            if ( lastValue < values[i] ):
                raise ValueError()
          
        return frequencies
        