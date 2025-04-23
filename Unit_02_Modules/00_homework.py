#################################################################################
# create a module named my_math with the following functions
# 1. factorial
# 2. square_root
# 3. cube_root

def factorial(x):
    factorial = 1
    if x <= 0:
        return None 
    else:
        for i in range(1,x + 1):
           factorial = factorial*i
        return factorial

# usage:
# factorial(23)

def square_root(x):
    return (x**(1/2))

# usage:
# square_root(49)

def cube_root(x):

    return round(x**(1/3))

# usage:
# cube_root(729)

#################################################################################
# use random module to simulate a die roll (get a random number between 1 and 6)

import random

def die_roll():
    return random.randint(1,6)

# usage:
# print(die_roll())

#################################################################################
# use datetime module to print todays date

import datetime

def today():
    return(datetime.datetime.now())
    
# usage:
# print(today())

#################################################################################
# use Counter from collections module, to find the frequency of each letter in a given sentence

from collections import Counter

def frequency(sentence):
    sentence = sentence.lower()
    char_count = Counter(sentence)  
    for char, count in sorted(char_count.items()):
        print(f"{char}: {count}")

# usage:
# frequency(sentence = "The quick brown fox jumps over the lazy dog.")
