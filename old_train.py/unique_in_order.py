

def unique_in_order(sequence):
    new_list = []
    current_item = None
    for item in sequence:
        if item != current_item:
            new_list.append(item)
            current_item = item
    return new_list
    
    
    
    
print(unique_in_order('AAAABBBCCDAABBB'))