# よく使う条件式
# == != >= > <= <
# 等価の条件式
x = 10
result = x == 10
print(result)
x = "Apple"
result = x == "Apple"
print(result)

# 比較の条件式
a = 10
b = 20
result = a >= b
print(result)

# 包含の条件式
x = 'A'
result = x in "Apple"
print(result)
x = "apple"
result = x in ["apple", "banana"]
print(result)

# and,or,not
x = "Apple"
y = "Banana"
result = (x == "Apple") and (y == "Banana")
print(result)
result = (x == "elppA") or (y == "Banana")
print(result)
result = not(x == "Apple")
print(result)