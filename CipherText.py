# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 00:28:37 2020

@author: Anubha Khurana
"""
"""
For example,

cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same) 

({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')

"""

def decodeChar(dict_map, i):
    char = ""
    
    for item in dict_map.items():
        if(item[1] == i):
            char = item[0]
            break
    
    return char

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
       
    dict_map = {}
    
    j = 0
    for i in map_from:
        dict_map[i] = map_to[j]
        j += 1
    
    
    decodedString= ""
    for i in code:
        decodedString += decodeChar(dict_map, i)
    
    returnTuple = (dict_map, decodedString)
    
    return returnTuple
    
print(cipher("abcd", "dcba", "dab"))