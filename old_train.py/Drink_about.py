def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age < 18 and age >= 14:
        return 'drink coke'
    elif age < 21 and age >= 18:
        return 'drink beer'
    else:
        return 'drink whisky'
    
    
# Alccol is prohibited by the islamic religion its only for the practice
print(people_with_age_drink(13))
print(people_with_age_drink(17))
print(people_with_age_drink(18))
print(people_with_age_drink(20))
print(people_with_age_drink(30))


    