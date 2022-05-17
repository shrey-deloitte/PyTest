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