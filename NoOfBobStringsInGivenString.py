# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:36:12 2020

@author: Anubha Khurana
"""

s = 'uocvboobobobobyxjoboobobbobob'
count = 0
strToLookFor = "bob"

index = 0
while index < len(s):
    bobFound = s.find(strToLookFor, index)
    if(bobFound != -1):
        count += 1
        index = bobFound + len(strToLookFor) - 1
    else:
        index += 1

print ("Number of times bob occurs is: " , count)
        
    