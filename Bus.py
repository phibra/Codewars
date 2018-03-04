# https://www.codewars.com/kata/number-of-people-in-the-bus

def number(bus_stops):
    people = 0
    
    for i in bus_stops:
        people += i[0] - i[1]
        
    return people
