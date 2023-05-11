import re

def abbreviate(s):
    abrv_s = re.findall(r"[A-Za-z]+|\W+|[0-9]", s)
    num_char = []
    for ltr in abrv_s:
        if len(ltr)>3 and ltr.isalpha():
            l = len(ltr) -2
            num_char.append(f"{ltr[0]}{l}{ltr[-1]}")
        else:
            num_char.append(ltr)
    return "".join(num_char)
            
    
#using REGEX to find all types of characteres in s
#l is local variable contains the number of hidens char
#then use a f"" format string an join it   
        



print(abbreviate('abbreviation'))
print(abbreviate('accessibility'))
print(abbreviate('Accessibility'))
print(abbreviate('elephant-ride'))
