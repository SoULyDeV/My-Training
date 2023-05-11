def stray(arr):
    for i in arr:
         if arr.count(i) == 1:
            return i
# the built-in function count() returns the number of times a value appears in an array.
# so here if i appear once we return it

print(stray([1,1,2]))
print(stray([17, 17, 3, 17, 17, 17, 17]))