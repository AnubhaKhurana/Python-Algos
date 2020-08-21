# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:36:12 2020

@author: Anubha Khurana
"""

s = 'azcbobobegghaklO'
count = 0

for letters in s:
    if(letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u'):
        count += 1
    if(letters == 'A' or letters == 'E' or letters == 'I' or letters == 'O' or letters == 'U'):
        count += 1
print (count)
        
    