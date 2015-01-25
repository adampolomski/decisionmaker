'''
Created on 25 sty 2015

@author: Adam Polomski
'''
import unittest
from probability import distribution

class DistributionTest(unittest.TestCase):
    
    
    def testShouldCalculateProbabilities(self):
        # given
        frequencies = {1: 1, 2: 7, 3: 19, 4: 37, 5: 61, 6: 91}
        
        # when
        probabilities = distribution.Distribution.probabilitiesFromFrequencies(frequencies)
        
        # then
        self.assertSequenceEqual(probabilities, {1: 0.004629629629629629, 2: 0.032407407407407406, 3: 0.08796296296296297, 4: 0.1712962962962963, 5: 0.2824074074074074, 6: 0.4212962962962963}, "Invalid probabilities.", None)
        
    def testShouldCalculateZeroProbabilities(self):
        # given
        frequencies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        
        # when
        probabilities = distribution.Distribution.probabilitiesFromFrequencies(frequencies)
        
        # then
        self.assertSequenceEqual(probabilities, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, "Invalid probabilities.", None)
    
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
