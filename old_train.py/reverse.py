def reverse_words(text):
    
    new_words = text.split(' ')
    reversed_words = []
    for word in new_words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)
    
 


#function reverse a string

print(reverse_words('This is an example'))
