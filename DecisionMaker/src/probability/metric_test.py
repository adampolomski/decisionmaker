'''
Created on 25 sty 2015

@author: Adam Polomski
'''

import unittest
from probability.metric import ExpectedValue, Variation, StandardDeviation


class MetricTest(unittest.TestCase):


    def testShouldCalculateExpectedValue(self):
        # given
        metric = ExpectedValue()
        probabilities = {1: 0.004629629629629629, 2: 0.032407407407407406, 3: 0.08796296296296297, 4: 0.1712962962962963, 5: 0.2824074074074074, 6: 0.4212962962962963}
        
        # when
        expectedValue = metric.calculate(probabilities)
        
        # then
        self.assertEqual(expectedValue, 4.958333333333333, "Invalid expected value.")
        
    def testShouldCalculateVariation(self):
        # given
        metric = Variation()
        probabilities = {1: 0.004629629629629629, 2: 0.032407407407407406, 3: 0.08796296296296297, 4: 0.1712962962962963, 5: 0.2824074074074074, 6: 0.4212962962962963}
        
        # when
        variation = metric.calculate(probabilities)
        
        # then
        self.assertEqual(variation, 25.89351851851852, "Invalid variation.") 
        
    def testShouldCalculateStandardDeviation(self):
        # given
        metric = StandardDeviation()
        probabilities = {1: 0.004629629629629629, 2: 0.032407407407407406, 3: 0.08796296296296297, 4: 0.1712962962962963, 5: 0.2824074074074074, 6: 0.4212962962962963}
       
        # when
        standardDeviation = metric.calculate(probabilities)
        
        # then
        self.assertEqual(standardDeviation, 5.088567432835937, "Invalid standard deviation.")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()