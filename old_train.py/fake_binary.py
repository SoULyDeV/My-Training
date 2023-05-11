def fake_bin(x):
    
    new_lst = ''
    for num in x:
        if int(num) < 5:
            new_lst += '0'
        else:
            new_lst += '1'

    return new_lst
    

# best practice return ''.join('0' if c < '5' else '1' for c in x)

print(fake_bin('588832199'))