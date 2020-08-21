# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:36:12 2020

@author: Anubha Khurana
"""

s = 'msemaouy'
lengthOfLongestString = 0
longestString = ""

index = 0
startIndex = 0
while index < len(s)-1:
    if(ord(s[index]) > ord(s[index+1])):
        if(len(s[startIndex:index+1]) > len(longestString)):
            longestString = s[startIndex:index+1]
            print('longestString: ', longestString)
        startIndex = index+1
        print(' startIndex: ', startIndex)
    elif(index == len(s)-2):
        print('index: ', index)
        if(len(s[startIndex:index+2]) > len(longestString)):
            longestString = s[startIndex:index+2]
            print('2: ', longestString)
    index += 1

if(longestString == ""):
    longestString = s
    

print("Longest substring in alphabetical order is:", longestString)
        
    