# round() in python3.10
print(round(2.22222, 2))    # 2.22
print(round(5.555, 5))  # 5.555
print(round(2.55, 1))   # 2.5
print(round(2.56, 1))   # 2.6
print(round(2.5, 0))    # represent as float, 2.0
print(round(2.6, 0))    # represent as float, 3.0
print(round(-2.5, 0))   # represent as float, -2.0
print(round(-2.6, 0))   # represent as float, -3.0
print(round(2.0, 0))    # represent as float
print(round(2, 0))  # represent as int
print(round(2, 3))  # represent as int
print(round(-2, 3)) # same as positive

# My comprehension about round() function
# Last compared bit >=6: Round up, <=5: Round down, represent as float/int when the original number is float/int

# The result of round() function linked to version of Python
# The actual value we save usually less than it's original value (save as binary causes lower accuracy)
# Avoid using round() function due to it's low accuracy
# We can use function in "import math", or the numeric operation Python have
