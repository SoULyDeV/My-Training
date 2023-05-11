
def maskify(cc):
    last_cc =  cc[-4:]
    hash_cc = len(cc) - len(last_cc)
    if len(cc) > 4 :
        return  "#" * hash_cc + last_cc
    else:
        return cc
    



print(maskify("4455667346745"))