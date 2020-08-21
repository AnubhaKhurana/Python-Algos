# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:33:22 2020

@author: Anubha Khurana
"""

from math import tan, pi
   

def polysum(n, s):
    '''
    Parameters
    ----------
    n : Number of sides of a polygon.
    s : Length of each side of a polygon.

    This function should sum the area and square of the perimeter of the regular polygon. 
    Returns
    -------
    This function return the sum, rounded to 4 decimal places

    '''
     
    areaOfPolygon = (0.25 * n * s * s)/ tan(pi/n)
    
    periOfPolygon = s * n
    
    returnValue = areaOfPolygon + periOfPolygon ** 2
    
    return float("{0:.4f}".format(returnValue))

print(polysum(5, 4))
    
    