# https://www.codewars.com/kata/string-cleaning/

def string_clean(s):
    output = ""
    
    for symbol in s:
        if not(symbol.isdigit()):
            output += symbol
            
    return output
