import string

def is_uppercase(inp):
    special_chars = string.punctuation
    return inp.isupper() if inp not in special_chars else True
#best practice: return inp.upper()==inp





print(is_uppercase("hello"))
print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("HELLO I AM DONALD"))
print(is_uppercase("$%&"))
print(is_uppercase("HELLO"))
