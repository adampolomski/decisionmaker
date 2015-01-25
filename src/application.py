'''
Created on 25 sty 2015

@author: Adam Polomski
'''
import sys
from model import TwoCriteriaModelFactory

if __name__ == '__main__':
    
    # Larger alpha, more prone to taking risks
    alpha = 2.5  
    
    # Number of weeks in a year .... more or less
    rolls = 12 * 4 
    
    # Matches with values formatted as "(FemaleArtist,MaleArtist,value)".
    # Ordered decreasingly on the match value.
    path = "C:/data.txt"
    
    # Initiating model  
    factory = TwoCriteriaModelFactory(alpha)
    
    
    # Loading data, building dictionary
    f = open(path, 'r')
    
    matches = {}
    values = []
    for line in f:
        line = line[1:-2]
        parts = line.split(',')
        matches.setdefault(parts[0] + ',' + parts[1], int(parts[2]))
        values.append(int(parts[2]))
    
    # Reading input, calculating
    for line in sys.stdin:
        model = factory.createModel(values, rolls)
        curVal = matches.get(line[:-1])
        
        if model.goForIt(curVal):
            print("yes")
            break
        else:
            print("no")
            
        rolls = rolls - 1
