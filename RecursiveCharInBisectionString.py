# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:12:56 2020

@author: Anubha Khurana
"""


def isIn(char, aStr):

       
    if aStr == '':
        return False
    m = aStr[len(aStr) // 2]
    if(char == m):
        return True
    elif len(aStr) == 1:
        return False 
    else:
        if char < m:
            return isIn(char, aStr[:len(aStr) // 2])
        elif char > m:
            return isIn(char, aStr[len(aStr) // 2:])
    return isIn(char, aStr)
    
    
print(isIn('s', "bcjlmpqruvwz"))