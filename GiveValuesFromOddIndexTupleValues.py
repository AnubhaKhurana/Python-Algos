# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:47:45 2020

@author: Anubha Khurana
"""


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    
    newTuple = ()
    
    for position  in range(1, len(aTup) + 1):
        oddPosition = position % 2
        if(oddPosition == 1):
            newTuple = newTuple + aTup[position - 1 : position]
    
    return newTuple
 
aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))