# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:12:48 2020

@author: Anubha Khurana
"""


balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
monthlyLowerBound = balance / 12
monthlyUpperBound = (balance * (1 + monthlyInterestRate) ** 12)/12.0

minimumBalance = (monthlyLowerBound + monthlyUpperBound)/2
remainingBalance = balance - minimumBalance

while monthlyUpperBound - monthlyLowerBound > 0.01 :
    
    minimumBalance = (monthlyLowerBound + monthlyUpperBound)/2    
    remainingBalance = balance - minimumBalance
    
    for month in range(1, 12):
        monthlyInterestThisMonth = remainingBalance * monthlyInterestRate
        remainingBalance = remainingBalance + monthlyInterestThisMonth - minimumBalance
        
    if remainingBalance < 0.01:
        monthlyUpperBound = minimumBalance
    elif remainingBalance > 0.01:
        monthlyLowerBound = minimumBalance
    
print("Lowest Payment: " , str("{0:.2f}".format(minimumBalance)))

