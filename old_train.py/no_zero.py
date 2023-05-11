def no_boring_zeros(n):
    if n == 0:
        return 0
    else:
        n = str(n)
        while n[-1] == "0":
            n = n[:-1]
        return int(n)
    
# while n-1 == 0 will loop to number != 0  


print(no_boring_zeros(1450))
print(no_boring_zeros(960000))
print(no_boring_zeros(1050))
print(no_boring_zeros(-100))
print(no_boring_zeros(2016))
print(no_boring_zeros(0))