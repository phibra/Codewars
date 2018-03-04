# https://www.codewars.com/kata/how-good-are-you-really

def better_than_average(class_points, your_points):
    counter = 0
    sum = 0
    output = True
    
    for i in class_points:
        sum += i
        counter += 1
    
    if sum / counter >= your_points:
        output = False
    
    return output
