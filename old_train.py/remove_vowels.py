def shortcut( s ):
    for l in 'aeiou':
        s = s.replace(l, '')
    return s



print(shortcut('hello'))
    
    