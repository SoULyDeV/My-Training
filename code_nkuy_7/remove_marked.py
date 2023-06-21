#Define a method/function that removes from a given array of integers all the values contained in a second array.


class List:
    def remove_(self, integer_list, values_list):
        result = [x for x in integer_list if x not in values_list]
        return result