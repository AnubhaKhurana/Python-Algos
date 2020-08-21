# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:41:03 2020

@author: Anubha Khurana
"""


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    smallerNumber = b
    if a < b:
        smallerNumber = a
    
    for i in range(smallerNumber, 0, -1):
        remainder = a % i
        if(remainder > 0):
            continue
        else:
            remainder = b % i
            if(remainder > 0):
                continue
            else:
                break
            
    return i

print(gcdIter(17, 12))