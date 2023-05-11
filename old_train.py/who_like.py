def likes(names):
    if len(names) == 0:
        return "No one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this" 
    elif len(names) >= 4:
        return names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"

    
    # your code here
    



print(likes([]))
print(likes(['Adrew']))
print(likes(['Adrew', 'Jeff', 'Thomas']))
print(likes(['Adrew', 'jeff']))
print(likes(['Adrew', 'jeff','Eric', 'Jeff']))
print(likes(['Adrew', 'jeff','Eric', 'Jeff', 'Sebastian']))