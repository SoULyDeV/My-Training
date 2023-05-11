def remove_last(s):
    return s[:-1] if s.endswith('!') else s
    
    
print(remove_last('Hello world!'))
print(remove_last('Hello world!!'))