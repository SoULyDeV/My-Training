def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []
    
    count_positives = 0
    sum_negatives = 0
    
    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num
    
    return [count_positives, sum_negatives]



print(count_positives_sum_negatives([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]))
print(count_positives_sum_negatives([0, 0]))