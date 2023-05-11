def isogam(string):
    return len(string) == len(set(string))



#set() will give us a new version of the string without duplicates, because sets in python not allowed duplicate items

print(isogam('aba'))
print(isogam('maroce'))
print(isogam('alpara'))
print(isogam('alpAra'))