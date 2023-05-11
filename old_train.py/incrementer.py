def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


print(increment_string('loop99'))
print(increment_string('lunep001'))
print(increment_string('linp32'))
print(increment_string('loup'))