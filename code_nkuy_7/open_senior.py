'''
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

'''






def open_or_senior(data):
    output = []
    for members in data:
        age = members[0]
        handicap = members[1]
        
        if age >= 55 and handicap > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output
   


print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))

#Best practice
''' def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
'''