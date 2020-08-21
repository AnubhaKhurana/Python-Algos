# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:02:17 2020

@author: Anubha Khurana
"""

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    
    remainder = 1
    return remainder == x % 2

x = 8
print(odd(x))
