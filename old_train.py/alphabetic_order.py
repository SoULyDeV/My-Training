def alphabetic(s):
    return list(s) == sorted(s)
    
#list() will give us a list of letters then we will compare it with sorted() 
    
print(alphabetic('doors')) 
print(alphabetic('kata')) 