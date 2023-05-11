def passed(lst):
    new_lst = 0
    passed = 0
    average = 0
    for n in lst:
        if n < 19 :
            new_lst += n
            passed += 1
            average = new_lst / passed
       
    if passed == 0:
        return 'No pass scores registered.'
    else:
        return  average 
    
     
    



print(passed([10,10,10,18,20,20] ))
print(passed([22,20,20] ))


# best practice
#def passed(lst):
#    a = list(filter(lambda x: x<=18, lst))
#    return 'No pass scores registered.' if a == [] else round(sum(a)/len(a))