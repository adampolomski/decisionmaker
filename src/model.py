'''
Created on 25 sty 2015

@author: Adam Polomski
'''
import math
from probability.distribution import Distribution
from probability.metric import StandardDeviation, ExpectedValue, Metric

class Model(object):
    '''
    '''
    
    def __init__(self, distribution, metric):
        self.distribution = distribution
        self.metric = metric
        
    def goForIt(self, curVal):
        potVal = self.distribution.metric(self.metric)
        curVal = self.metric.agregate(curVal, 0)
        return potVal <= curVal
    
class ModelFactory(object):
    '''
    classdocs
    '''
    
    def createModel(self, values, rolls):
        pass    
       
class TwoCriteriaModelFactory(ModelFactory):
    
    def __init__(self, alpha):
        self.alpha = alpha
     
    def createModel(self, values, rolls):
        frequencies = TwoCriteriaModelFactory.valueFrequency(values, rolls)
        distribution = Distribution(Distribution.probabilitiesFromFrequencies(frequencies))
        gain = ExpectedValue()
        risk = StandardDeviation()
        return Model(distribution, AgregateMetric(self.alpha, gain, risk)) 
    
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

class AgregateMetric(Metric):
    def __init__(self, alpha, gain, risk):
        self.alpha = alpha
        self.gain = gain
        self.risk = risk
        
    def calculate(self, probabilities):
        gain = self.gain.calculate(probabilities)
        risk = self.risk.calculate(probabilities)
        
        print(gain)
        print(risk)
        return self.agregate(gain, risk)
    
    def agregate(self, gain, risk):
        return self.alpha * gain - risk