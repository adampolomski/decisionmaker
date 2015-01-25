'''
Created on 25 sty 2015

@author: Adam Polomski
'''

import unittest
from probability import model

class ProbabilisticModelTest(unittest.TestCase):


    def setUp(self):
        self.model = model.ProbabilisticModel()


    def tearDown(self):
        pass


    def testShouldCalculateValueFrequency(self):
        #given
        values = [6, 5, 4, 3, 2, 1]
        rolls = 3
        
        #when
        frequency = model.ProbabilisticModel.valueFrequency(values, rolls)
        
        #then
        self.assertSequenceEqual(frequency, {1: 1, 2: 7, 3: 19, 4: 37, 5: 61, 6: 91}, "Invalid frequency dictionary.", None)
        
    def testShouldCalculateValueFrequencyWithDuplicaes(self):
        #given
        values = [6, 5, 4, 3, 3, 1]
        rolls = 3
        
        #when
        frequency = model.ProbabilisticModel.valueFrequency(values, rolls)
        
        #then
        self.assertSequenceEqual(frequency, {1: 1, 3: 26, 4: 37, 5: 61, 6: 91}, "Invalid frequency dictionary.", None)
        
    def testShouldFailOnUnorderedValues(self):
        #given
        values = [5, 6, 4, 3, 2, 1]
        rolls = 3
        
        #then
        self.assertRaises(ValueError, model.ProbabilisticModel.valueFrequency, values, rolls)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()