'''
Created on 25 sty 2015

@author: Adam Polomski
'''

import math

class Distribution(object):
    '''
    classdocs
    '''

    def __init__(self, probabilities):
        '''
        Constructor
        '''        
        self.probabilities = probabilities
        
    def metric(self, strategy):
        '''
        '''
        return strategy.calculate(self.probabilities)

    @staticmethod
    def probabilitiesFromFrequencies(frequencies):
        '''
        '''
        
        omega = sum(frequencies.values())
        probabilities = {}
        
        for key, val in frequencies.items():
            probabilities.setdefault(key, val / omega)
            
        return probabilities
    
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
            
            if (lastValue < values[i]):
                raise ValueError()
          
        return frequencies
        
class Metric:
    def calculate(self, probabilities):
        pass

class ExpectedValue(Metric):
    def calculate(self, probabilities):
        expectedValue = 0
        
        for value, probability in probabilities.items():
            expectedValue += value * probability
            
        return expectedValue
    
class Variation(Metric):
    def calculate(self, probabilities):
        expectedValue = ExpectedValue.calculate(self, probabilities)
        variation = 0
        
        for value, probability in probabilities.items():
            variation += math.pow(value, 2) * probability
            
        variation - math.pow(expectedValue, 2)
        return variation
        
class StandardDeviation(Metric):
    def calculate(self, probabilities):
        return math.sqrt(Variation.calculate(self, probabilities))