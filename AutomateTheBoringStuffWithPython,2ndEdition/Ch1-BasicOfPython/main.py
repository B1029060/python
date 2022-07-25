# Expression
# Numeric Operaion
# ** (1st) > % >= // (2nd) > / >= * (3rd) > - >= + (4th)
# Datatype
# int, float, str
# String combine and String copy
print("Alice" + "Bob") # String combine
print("Alice" * 5) # String copy
# TypeError: 1. "str" + "not str" 2. "str" * "not int" or "float"

# Variable and Value
# Assignment statement
# Variable = Value(Assign value to variable)
spam = 40
eggs = 2
print(spam + eggs)
print(spam + eggs + spam)
spam = spam + 2
print(spam)
# Overwriting
spam = "Hello"
print(spam)
spam = "Goodbye"
print(spam)
# Name of variable
# Rule of naming variable
# 1. A str or a char 2. using English, Number, and _ 3. Can't start with Number
# Camelcase: lookLikeThis
# Underscores:look_like_this
# Official Python Coding Style: PEP8

# First program
# This program says hello and asks fir my name

print("Hello World")
print("What is your name?") # ask for their name
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is:")
print(len(myName))
print("What is your age?")  # ask for their age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")
# Comments: telling what do you do in this row
# print(): print the content inside ()
# input(): to get the string user inputed
# len(): to get the length of string, numbers of element in list, dict, and so on
# str(), int(), float(): change the datatype into string, integer, and floating point
# int(9.99) == 9
# 42 != "42", 42 == 42.0, 42.0 == 0042.000


# Extension
# Find description document of len() by "Build-in Functions" website
# Get through round() function and try it

# max_size: in n-bits platform, its max size is (2 ** (n-1)) - 1
# When x in len(x) over max_size, it came out OverflowError
