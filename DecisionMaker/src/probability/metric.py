'''
Created on 25 sty 2015

@author: Adam Polomski
'''

import math

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