# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:33:42 2020

@author: Anubha Khurana
"""


def biggest(aDict):
    
    dictWithNumber = {}
    if(len(aDict) == 0):
        return ''    
    elif(len(aDict) == 1):
        return list(aDict.keys())[0]
    
    for i in aDict:
        valuePerKey = len(aDict[i])
        dictWithNumber[i] = valuePerKey
        
    allValuesInList = dictWithNumber.values()    
    maxValue = max(allValuesInList)
    
    for animals, numbers in dictWithNumber.items():
        if numbers == maxValue:
            return animals
    

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))