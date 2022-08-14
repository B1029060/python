# 数値演算
# +、-、*、/（四則演算）　**（べき乗）　％（mod)　//（切り捨て割り算）
calc = 5 ** 2
print(calc)
calc = 5 ** -2
print(calc)
calc = 5 // 2
print(calc)
calc = 5 / 2
print(calc)

# 優先順位
# 1.括弧の中　2.べき乗　3.掛け算、割り算、割り算余り　4.足し算、引き算
calc = 3 + 6 * (1 + 1 * 2) ** 2
print(calc)