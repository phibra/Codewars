# https://www.codewars.com/kata/find-nearest-square-number/

import math

def nearest_sq(n):    
    smallerNumber = math.floor(math.sqrt(n))
    biggerNumber = math.ceil(math.sqrt(n))
    
    if abs((smallerNumber ** 2) - n) > abs((biggerNumber ** 2) - n):
        return biggerNumber ** 2
    if abs((smallerNumber ** 2) - n) < abs((biggerNumber ** 2) - n):
        return smallerNumber ** 2
    else:
        return n
