'''
Created on 25 sty 2015

@author: Adam Polomski
'''
import sys
from model import TwoCriteriaModelFactory

if __name__ == '__main__':
    
    #parameters
    alpha = 2.5
    factory = TwoCriteriaModelFactory(alpha)
    rolls = 3
    
    #build dictionary
    path = "C:/Users/Nimbuzz/Downloads/job_1421736139483_0040_result.txt"
    f = open(path, 'r')
    
    matches = {}
    values = []
    for line in f:
        line = line[1:-2]
        parts = line.split(',')
        matches.setdefault(parts[0] + ' ' + parts[1], int(parts[2]))
        values.append(int(parts[2]))
    
    for line in sys.stdin:
        model = factory.createModel(values, rolls)
        curVal = matches.get(line[:-1])
        print("yes" if model.goForIt(curVal) else "no")
        rolls = rolls - 1