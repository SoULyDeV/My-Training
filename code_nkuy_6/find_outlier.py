'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
'''

def fint_outlier(integers): 
    odd = []
    even = []
    
    for n in integers:
        if n % 2 != 0:
            odd.append(n)
        elif n % 2 == 0:
            even.append(n)
    if len(odd) < len(even):
        return odd[0]
    else:
        return even[0]




print(fint_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))