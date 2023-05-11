def two_sum(numbers, target):
    for n in range(len(numbers)):
        for a in range(n + 1, len(numbers)):
            if numbers[n] + numbers[a] == target:
                return [n, a]
#Nested loop       


print(two_sum([1, 2, 3], 4))
print(two_sum([2, 2, 3], 4))