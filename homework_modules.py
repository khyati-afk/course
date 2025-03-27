def factorial(x):

    factorial = 1
    if x <= 0:
        return None 
    else:
        for i in range(1,x + 1):
           factorial = factorial*i
        return factorial

factorial(23)

        
##################################################################

def square_root(x):

    return (x**(1/2))

square_root(49)


##################################################################

def cube_root(x):

    return round(x**(1/3))

cube_root(729)


##################################################################

import random

def die_throw():

    return random.randint(1,6)

print(die_throw())


##################################################################

import datetime

def today():
    
    return(datetime.datetime.now())
    
today()


##################################################################

from collections import Counter

def frequency():

    sentence = input("Enter a sentence: ")

    sentence = sentence.lower()

    char_count = Counter(sentence)  

    for char, count in sorted(char_count.items()):
        print(f"{char}: {count}")

frequency()
