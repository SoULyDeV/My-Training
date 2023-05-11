def high(x):
    arr,numArr= x.split(' '),[]
    for val in arr:
        intNum = 0
        letters = list(val)
        for word in letters:
            #ord() function returns the ASCII value of a character
            intNum += ord(word) - 96
        numArr.append(intNum)
    return arr[numArr.index(max(numArr))]


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))


#our task is to find the highest word in a string according to the alphabetical order
#example: a = 1 b = 2 c = 3 d = 4 e = 5 f = 6
#abad = 1 + 2 + 1 + 4 = 8
#