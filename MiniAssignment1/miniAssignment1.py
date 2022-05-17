from collections import Counter
from itertools import combinations

#question 1
class StringClass:

    def __init__(self, value):
        self.str = value

    def length_of_string(self):
        return len(self.str)

    def string_to_list(self, value):
        list1 = list(value)
        return list1

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

#question 4
class EqualSumPairs:

    def count(self, list1):
        list2 = []
        for i in list1:
            res = 0
            for j in i:
                res += int(j)
            list2.append(res)
        return len(set(list2))


value1 = input("Enter first String: ")
obj1 = StringClass(value1)
print("Length of the String: ")
print(obj1.length_of_string())
print("List of String: ")
print(obj1.string_to_list(value1))

value2 = input("Enter second String: ")
obj2 = PairsPossible(value2)
list1 = obj2.pairs()
print("Pairs Possible are: ")
print(list1)

obj3 = SearchCommonElements(value1, value2)
print("Common Elements are: ")
print(obj3.commonElements())

obj4 = EqualSumPairs()
length = obj4.count(list1)
print("Count of unique sums: ")
print(length)