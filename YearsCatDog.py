# https://www.codewars.com/kata/cat-years-dog-years/

def human_years_cat_years_dog_years(human_years):
    
    if human_years == 1:
        catYears = 15;
        dogYears = 15;
    elif human_years == 2:
        catYears = 15 + 9;
        dogYears = 15 + 9;
    else:
        catYears = 15 + 9 + 4 * (human_years - 2);
        dogYears = 15 + 9 + 5 * (human_years - 2);
        
    return [human_years, catYears, dogYears]
