'''
The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

'''

def narcissistic(value):
    
    num_digits = len(str(value))
    sum = 0
    
    for num in str(value):
        sum += int(num) ** num_digits
    
    return sum == value


print(narcissistic(7))
print(narcissistic(153))