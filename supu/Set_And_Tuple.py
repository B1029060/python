# 集合とタプル

# 集合とは？
# Pythonの型の1つで、複数の値を持っています（リストと同じ部分）
# 順序が存在しない、重複した値を持てない（リストと異なる部分）

# タプルとは？
# Pythonの型の1つで、複数の値を持っていて、順序が存在する（リストと同じ部分）
# 変更できない（リストと異なる部分）


# 集合について
x_set = {11, 222, 333}

y_list = [11, 333, 444, 555, 11]
y_set = set(y_list) # リストを集合に変換

print(x_set)
print(y_set)    # 重複した値が集合変換され1つになった

result = x_set & y_set  # 積集合
print(result)
result = x_set - y_set  # 差集合
print(result)
result = x_set | y_set  # 和集合
print(result)


# タプルについて
x_tuple = (1, 3, 5)

y_list = [3, 4, 5]
y_tuple = tuple(y_list) # リストをタプルに変換

print(x_tuple)
print(y_tuple)

result = x_tuple[2] # タプルに順序があり、インデックスで要素を指定できます
print(result)

# タプルが変更できないため、エラー出ます
# extend,　removeも同様にエラー出ます
'''
result = x_tuple.append(4)
print(result)
'''

result = x_tuple + y_tuple  # 複数のタプルを結合
print(result)

def test_function():
    x = 2 * 2
    y = 3 * 3
    return x, y
result1, result2 = test_function()
print(result1, result2)
result1 = test_function()   # 戻り値がタプルとして記録します
print(result1)

x_dict = {'a': 100, 'b': 200, 'c': 300}
for x in x_dict.items():    # タプル("キー", "値")として記録
    print(x)
    print(x[0]) # タプルのキーを取得
    print(x[1]) # タプルの値を取得

# まとめ
'''
　　　　|   順序  |   重複  |   変更
リスト　|   あり  |   ＯＫ  |   ＯＫ
集合　　|   なし  |   ＮＧ  |   ＯＫ
タプル　|   あり  |   ＯＫ  |   ＮＧ
'''
