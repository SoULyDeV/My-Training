def to_jaden_case(string):
    new_string = string.split()
    new_string = [w.capitalize() for w in new_string]
    return " ".join(new_string)
    
# best practice : return ' '.join(map(str.capitalize, string.split()))



print(to_jaden_case("How can mirrors be real if our eyes aren't real"))