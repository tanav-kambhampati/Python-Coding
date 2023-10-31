import random
import sys

print("Which range of numbers would you like to play?")
rangeLimit = int(input("How many numbers do you want to go to?"))
gameRunning = True

def guess():
    global rangeLimit
    number = random.randint(0, rangeLimit) 
    guess1 = int(input("Enter your guess for what the number is:"))
    if guess1 == number:
        print("Good Job! You guessed the number correctly")
        play = int(input("Would you like to play again? Press 1 to play again"))
        if play > 2 or play < 0: 
            print("This is not valid")
        if play == 1:
            print("Which range of numbers would you like to play?")
            rangeLimit = int(input("How many numbers do you want to go to?"))
            gameRunning = True           
            guess()
        else:
            sys.exit
    else:
        print("Sorry, but that is not the number I have in mind. Try again")
        gameRunning = True
        guess()

if gameRunning == True:
    guess()
# IT WORKS!!!!!!!!!