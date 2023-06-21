def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= len(signature):
        return signature[:n]

    result = signature[:]
    while len(result) < n:
        next_number = sum(result[-3:])
        result.append(next_number)

    return result


print(tribonacci([1, 1, 1], 10))
# Output: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

print(tribonacci([0, 0, 1], 10))
# Output: [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]

print(tribonacci([1, 2, 3], 5))
# Output: [1, 2, 3, 6, 11]