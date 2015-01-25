'''
Created on 25 sty 2015

@author: Adam Polomski
'''

import unittest
from probability import distribution
from probability.distribution import ExpectedValue, Variation, StandardDeviation

class DistributionTest(unittest.TestCase):


    def setUp(self):
        self.model = distribution.Distribution({1: 0.004629629629629629, 2: 0.032407407407407406, 3: 0.08796296296296297, 4: 0.1712962962962963, 5: 0.2824074074074074, 6: 0.4212962962962963})


    def tearDown(self):
        pass
    
    def testShouldCalculateExpectedValue(self):
        # given
        metric = ExpectedValue()
        
        # when
        expectedValue = self.model.metric(metric)
        
        # then
        self.assertEqual(expectedValue, 4.958333333333333, "Invalid expected value.")
        
    def testShouldCalculateVariation(self):
        # given
        metric = Variation()
        
        # when
        variation = self.model.metric(metric)
        
        # then
        self.assertEqual(variation, 25.89351851851852, "Invalid variation.") 
        
    def testShouldCalculateStandardDeviation(self):
        # given
        metric = StandardDeviation()
        
        # when
        standardDeviation = self.model.metric(metric)
        
        # then
        self.assertEqual(standardDeviation, 5.088567432835937, "Invalid standard deviation.")

    def testShouldCalculateProbabilities(self):
        # given
        frequencies = {1: 1, 2: 7, 3: 19, 4: 37, 5: 61, 6: 91}
        
        # when
        probabilities = distribution.Distribution.probabilitiesFromFrequencies(frequencies)
        
        # then
        self.assertSequenceEqual(probabilities, {1: 0.004629629629629629, 2: 0.032407407407407406, 3: 0.08796296296296297, 4: 0.1712962962962963, 5: 0.2824074074074074, 6: 0.4212962962962963}, "Invalid probabilities.", None)
        

    def testShouldCalculateValueFrequency(self):
        # given
        values = [6, 5, 4, 3, 2, 1]
        rolls = 3
        
        # when
        frequency = distribution.Distribution.valueFrequency(values, rolls)
        
        # then
        self.assertSequenceEqual(frequency, {1: 1, 2: 7, 3: 19, 4: 37, 5: 61, 6: 91}, "Invalid frequency dictionary.", None)
        
    def testShouldCalculateValueFrequencyWithDuplicaes(self):
        # given
        values = [6, 5, 4, 3, 3, 1]
        rolls = 3
        
        # when
        frequency = distribution.Distribution.valueFrequency(values, rolls)
        
        # then
        self.assertSequenceEqual(frequency, {1: 1, 3: 26, 4: 37, 5: 61, 6: 91}, "Invalid frequency dictionary.", None)
        
    def testShouldFailOnUnorderedValues(self):
        # given
        values = [5, 6, 4, 3, 2, 1]
        rolls = 3
        
        # then
        self.assertRaises(ValueError, distribution.Distribution.valueFrequency, values, rolls)
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
