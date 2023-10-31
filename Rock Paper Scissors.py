import random
import sys

def game():
    print("Press 1 to play unbeatable rock paper scissors")
    print("Press 2 to play normal rock paper scissors")

    unbeatable_normal = int(input("Which one would you like to play"))

    def choice():
        if unbeatable_normal > 2 or unbeatable_normal < 1:
            print("This is not valid") 
            choice()

    def unbeatable_rps():
        user_choice = str(input("Choose between rock, paper, and scissors. Please type your answer in all lowercase letters and with proper spelling"))
        if user_choice == "rock":
            print("The AI chose paper")
        if user_choice == "paper":
            print("The AI chose scissors")
        if user_choice == "scissors":
            print("The AI chose rock")
            def again(): 
                playagain = int(input("You Lost! Press one to play again and press 2 to stop"))
                if playagain == 1:
                    game()
                else:
                    sys.exit
        again()          

        if unbeatable_normal == 1:
            unbeatable_rps()

game()