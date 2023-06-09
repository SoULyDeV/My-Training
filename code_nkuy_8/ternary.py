def sale_hotdogs(n):
    if n < 5:
        return n*100
    elif n >= 5 and n < 10:
        return n*95
    else:
        return n*90
    

#Best practice: return n * (100 if n < 5 else 95 if n < 10 else 90)

print(sale_hotdogs(2))
print(sale_hotdogs(9))
print(sale_hotdogs(11))


"""
number of hotdogs	price per unit (cents)
n < 5 price	 100
n >= 5 and n < 10 price	95
n >= 10 price 90
"""