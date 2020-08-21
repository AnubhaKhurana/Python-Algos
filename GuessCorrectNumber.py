# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Please think of a number between 0 and 100!")

miniNumber = 0
maxiNumber = 100

guessCorrect = False

while guessCorrect == False:
   
    promptGuess = int((miniNumber + maxiNumber)/2)
    print("Is you secret number", str(promptGuess) + "?")     
    question = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
    promptString = input(question) 
    
    if promptString == 'l' :
        miniNumber = promptGuess
    elif promptString == 'h':
        maxiNumber = promptGuess
    elif promptString == 'c':
        guessCorrect = True
        break
    else:
        print("Sorry, I did not understand your input.")

        
if guessCorrect == True:
    print("Game over. Your secret number was: ", int(promptGuess))
        
        
            

