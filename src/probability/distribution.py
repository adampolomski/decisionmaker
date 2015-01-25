'''
Created on 25 sty 2015

@author: Adam Polomski
'''
class Distribution(object):
    '''
    Discrete probability distribution.
    '''

    def __init__(self, probabilities):
        '''
        Constructor
        '''        
        self.probabilities = probabilities
        
    def metric(self, strategy):
        '''
        Calculates probability distribution metric specified by given strategy.
        '''
        return strategy.calculate(self.probabilities)

    @staticmethod
    def probabilitiesFromFrequencies(frequencies):
        '''
        '''
        
        omega = sum(frequencies.values())
        probabilities = {}
        
        for key, val in frequencies.items():
            p = 0 if omega == 0 else val / omega
            probabilities.setdefault(key, p)
            
        return probabilities