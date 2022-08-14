# Pythonの文字列フォーマット
# 文字列フォーマットとは？
# 書式形式を指定、変数を埋め込むこと
# %演算子 formatメソッド（python3~） f文字列を使う（python3.6~）

# f文字列：変数の埋め込み
x = "山田"
y = "太郎"
result = f'{x}さん'
print(result)
result =f'{x + y}さん'
print(result)

# f文字列：形式の指定
# ゼロ埋め、金額用のカンマ区切り、小数点以下の桁数指定
# ゼロ埋め
x = 123
result = f'No: {x:010}'
print(result)
test = f'{str(2):002}'  # 対照組
print(test) # str型を代入すると、02ではなく20になります
# カンマ区切り
x = 9000000
result = f'{x:,}円あります'
print(result)
# 小数点桁数指定
x = 0.12
result = f'{x:.4f}'
print(result)
