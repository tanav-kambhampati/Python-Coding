import random
import time

secret_word = ["ball", "doll", "golf", "secret", "thief"]
word = random.choice(secret_word)
length = len(word)
name = input("What is your name: ")
print("welcome" + name + "! Best of Luck...")
time.sleep(2)
print("Test begins now!")
time.sleep(7)

count = 0
display = '*' * length


def hangman(count, display, word):
    limit = 3
    guess = input("The word is this:" + display + "Enter your guess: ")
    if guess in word:
        index = word.find(guess)
        word = word[:index] + "*" + word[index + l:]
        display = display[:index] + guess + display[index + l:]
    else:
        count+= 1
        if count == 1:
            print("Wrong input")