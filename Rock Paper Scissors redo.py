import random 

print("Press 1 to choose Rock. Press 2 for Paper. Press 3 for scissors")
choice = int(input())

if choice > 3 or choice <1:
    print("kys")
elif choice == 1:
    choice = "Rock"
elif choice == 2:
    choice = "Paper"
elif choice == 3:
    choice = "Scissors"

code_choices = ["Rock", "Paper", "Scissors"]
code_choice = random.choice(code_choices)
print("The AI chose " + code_choice)
if code_choice == choice:
    print("Oops! This is a tie")

if code_choice == "Rock" and choice == "Paper":
    print("Good Job! You won :)")
elif code_choice == "Scissors" and choice == "Rock":
    print("Good Job! You won :)")
elif code_choice == "Paper" and choice == "Scissors":
    print("Good Job! You won :)")
elif choice == "Rock" and code_choice == "Paper":
    print("Uh oh! You lost :(")
elif choice == "Scissors" and code_choice == "Rock":
    print("Uh oh! You lost :(")
elif choice == "Paper" and code_choice == "Scissors":
    print("Uh oh! You lost :(")

# IMPORTANT FEEDBACK FROM NISARG, I COULD remove the elif choice == 1 stuff at the beginning