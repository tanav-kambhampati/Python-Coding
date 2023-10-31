from cmath import pi
import random
import math

print("If you want to type radicals, put rad() around your radical number. Ex: rad(2)/2. Type undefined answers as und. (with a period at the end)")

while True:
    operations = ["sin", "cos", "tan"]
    angles = ["π/6", "π/4", "π/3", "π/2", "2π/3", "3π/4", "5π/6", "π", "7π/6", "5π/4", "4π/3", "3π/2", "5π/3", "7π/4", "11π/6", "2pi"]

    operation = random.choice(operations)
    angle = random.choice(angles)
    print(operation +  "(" + angle + ")")
    answer = input("Enter your answer: ")

    #Sine operations
    if operation == "sin" and angle == "π/6" and answer == "1/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "π/4" and answer == "rad(2)/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "π/3" and answer == "rad(3)/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "π/2" and answer == "1":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "2π/3" and answer == "rad(3)/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "3π/4" and answer == "rad(2)/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "5π/6" and answer == "1/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "π" and answer == "0":
        print("Congratulations, this is correct")
    elif operation == "sin" and angle == "7π/6" and answer == "-1/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "5π/4" and answer == "-rad(2)/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "4π/3" and answer == "-rad(3)/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "3π/2" and answer == "-1":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "5π/3" and answer == "-rad(3)/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "7π/4" and answer == "-rad(2)/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "11π/6" and answer == "-1/2":
        print("Congratulations, this is correct!")
    elif operation == "sin" and angle == "2π" and answer == "0":
        print("Congratulations, this is correct!")
    #Cosine functions
    elif operation == "cos" and angle == "π/6" and answer == "rad(3)/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "π/4" and answer == "rad(2)/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "π/3" and answer == "1/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "π/2" and answer == "0":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "2π/3" and answer == "-1/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "3π/4" and answer == "-rad(2)/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "5π/6" and answer == "-rad(3)/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "π" and answer == "-1":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "7π/6" and answer == "-rad(3)/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "5π/4" and answer == "-rad(2)/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "4π/3" and answer == "-1/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "3π/2" and answer == "0":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "5π/3" and answer == "1/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "7π/4" and answer == "rad(2)/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "11π/6" and answer == "rad(3)/2":
        print("Congratulations, this is correct!")
    elif operation == "cos" and angle == "2π" and answer == "1":
        print("Congratulations, this is correct!")
    #Tangent functions
    elif operation == "tan" and angle == "π/6" and answer == "rad(3)/3":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "π/4" and answer == "1":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "π/3" and answer == "rad(3)":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "π/2" and answer == "und.":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "2π/3" and answer == "-rad(3)":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "3π/4" and answer == "-1":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "5π/6" and answer == "-rad(3)/3":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "π" and answer == "0":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "7π/6" and answer == "rad(3)/3":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "5π/4" and answer == "1":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "4π/3" and answer == "rad(3)":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "3π/2" and answer == "und":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "5π/3" and answer == "-rad(3)":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "7π/4" and answer == "-1":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "11π/6" and answer == "-rad(3)/3":
        print("Congratulations, this is correct!")
    elif operation == "tan" and angle == "2π" and answer == "0":
        print("Congratulations, this is correct!")
    else: 
        print("This is incorrect")

