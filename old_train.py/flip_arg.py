def warn_the_sheep(queue):
# flip the order of the list to get the sheep at the end of the list (index)
    queue = queue[::-1]
    wolf_count = 0
    for i, animal in enumerate(queue):
        if animal == 'wolf':
            wolf_count = i
    if wolf_count == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return f"Oi! Sheep number {wolf_count}! You are about to be eaten by a wolf!"
                
            



print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))
print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf']))