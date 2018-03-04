# https://www.codewars.com/kata/folding-your-way-to-the-moon/

def fold_to(distance):
    foldCounter = 0
    thickness = 0.0001
    
    if distance < 0:
        return None
    
    while distance >= thickness:
        thickness *= 2
        foldCounter += 1
    
    return foldCounter
