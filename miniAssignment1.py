
from itertools import combinations
from collections import Counter

#question 1
class StringClass:

    def __init__(self, string):
        self.string = string

    def strlen(self):
        return len(self.string)

    def strToList(self, inputStr):
        return [char for char in inputStr]

stringClass = StringClass("hello")
print("length of the string :- ", stringClass.strlen())
print("String converted to list : - ", stringClass.strToList("123456"))



#question 2
class PairsPossible(StringClass):

    def __init__(self, value):
        self.str = value

    def pairs(self):
        pair = list(combinations(self.str, 2))
        return pair


#question 3
class SearchCommonElements:

    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def commonElements(self):
        dict1 = Counter(set(self.input1))
        dict2 = Counter(set(self.input2))
        combinedDict = dict(dict1.items() & dict2.items())
        common_elements = []
        for (key, val) in combinedDict.items():
            for i in range(0, val):
                common_elements.append(key)
        return common_elements


value2 = input("Enter second String: ")
obj2 = PairsPossible(value2)
list1 = obj2.pairs()
print("Pairs Possible are: ")
print(list1)