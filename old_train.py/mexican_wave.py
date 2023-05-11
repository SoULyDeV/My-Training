def wave(person):
    """
    result = []
    for index, man in enumerate(person):
        if man.isalpha():
            result.append(person[:index]+person[index].upper()+person[index+1:])
    return result
    """
    final_wave = []
    for i, c in enumerate(person):
        if c.isalpha():
            final_wave.append(person[:i]+c.upper()+person[i+1:])
    return final_wave
           

#return [ str[:i] + c.upper() + str[i+1:] for i, c in enumerate(str) if c.isalpha() ]

print(wave('hello'))
print(wave('a b'))
print(wave('hello'))