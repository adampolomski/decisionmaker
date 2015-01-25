'''
Created on 25 sty 2015

@author: Adam Polomski
'''
import unittest
from model import TwoCriteriaModelFactory, AgregateMetric
from unittest.mock import MagicMock
from probability.metric import Metric


class TwoCriteriaModelFactoryTest(unittest.TestCase):

    def testShouldCalculateValueFrequency(self):
        # given
        values = [6, 5, 4, 3, 2, 1]
        rolls = 3
        
        # when
        
        frequency = TwoCriteriaModelFactory.valueFrequency(values, rolls)
        
        # then
        self.assertSequenceEqual(frequency, {1: 1, 2: 7, 3: 19, 4: 37, 5: 61, 6: 91}, "Invalid frequency dictionary.", None)
        
    def testShouldCalculateValueFrequencyWithDuplicaes(self):
        # given
        values = [6, 5, 4, 3, 3, 1]
        rolls = 3
        
        # when
        frequency = TwoCriteriaModelFactory.valueFrequency(values, rolls)
        
        # then
        self.assertSequenceEqual(frequency, {1: 1, 3: 26, 4: 37, 5: 61, 6: 91}, "Invalid frequency dictionary.", None)
        
    def testShouldFailOnUnorderedValues(self):
        # given
        values = [5, 6, 4, 3, 2, 1]
        rolls = 3
        
        # then
        self.assertRaises(ValueError, TwoCriteriaModelFactory.valueFrequency, values, rolls)
        
        
class AgregateMetricTest(unittest.TestCase):
    def testShouldCalculateMetric(self):
        #given
        alpha = 5
        gain = Metric()
        gain.calculate = MagicMock(return_value=5)
        risk = Metric()
        risk.calculate = MagicMock(return_value=5)
        metric = AgregateMetric(alpha, gain, risk)
        
        #when
        result = metric.calculate({})
        
        #then
        self.assertEqual(result, 20, "Invalid result.")
    
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
