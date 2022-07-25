# 制御構文
# Pythonのif文とfor文

# if文とは？
# 条件分岐（もしも○○○だったら、○○○してください）
# if文の書き方
x = 5
if x >= 10:
    print("10以上")
elif x >= 0:
    print("10未満0以上")
else:
    print("0未満")

# for文とは？
# 繰り返し処理（○○回、○○○を繰り返す）
# for文の書き方
x_list = [100, 190, 2980]
for x in x_list:
    x_yen = str(x) + '円'
    print(x_yen)

x_dict = {"apple": 100, "banana": 350}
for key, value in x_dict.items():
    text = key + 'は' + str(value) + "円です"
    print(text)

for y in range(10):
    print(y)


