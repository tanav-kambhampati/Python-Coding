from cmath import pi
import random
import math

print("If you want to type radicals, put rad() around your radical number. Ex: rad(2)/2")

sin_dict = {'sin(π/6)' : '1/2', 'sin(π/4)' : 'rad(2)/2'}
question = random.choice(sin_dict.keys)
print(question)


