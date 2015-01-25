'''
Created on 25 sty 2015

@author: Nimbuzz
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
            frequencies.setdefault(values[i], eventCount)
            if ( lastValue < values[i] ):
                raise ValueError()
          
        return frequencies
        