def queue_time(customers, n):
    checkout_tills = [0]*n
    for customer in customers:
        checkout_tills[0] += customer
        checkout_tills.sort()
    return max(checkout_tills)

print(queue_time([2,3,10], 2))
print(queue_time([5,4,3], 1))
print(queue_time([10,3,3,2], 2))