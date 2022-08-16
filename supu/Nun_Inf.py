# 非数と無限大について
# 無限大とは
import sys
print((max_num := sys.float_info.max))   # 1.7976931348623157e+308
# これより大きい数字が無限大として扱う
print(max_num + 1)   # 1.7976931348623157e+308/桁落ち：二つの数の差があまりにも大きいため、小さい方が省略された
print(max_num * 2)    # inf
print(max_num * -2) # -inf
print((x := float('inf')))  # inf

# 非数とは
# 数値として扱うはずだったのに数値じゃないもの(例：inf - inf)
print(float('inf') - float('inf'))  # nun

# 使いどころ：nan判定
import math
y = float('nan')
print(math.isnan(y))

# Noneとは
# Noneオブジェクトの唯一の変数、何のデータもないの意味です
# ==は値の判定、isはオブジェクトの判定
if (z := None) is None: # オブジェクトの判定
    print('zはNoneです')
a = None
b = None
print(id(a), id(b)) # Same
print('if') if None else print('else')  # else/Falseと同じ扱い
