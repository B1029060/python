# 辞書の作成
fruit = {"リンゴ": 120, "バナナ": 300, "イチゴ": 450}
print(fruit)

# 特定のキーの値を取得
banana = fruit["バナナ"]
print(banana)

# 辞書に要素を追加
fruit["トマト"] = 340
print(fruit)

# 特定のキーの値を変更
fruit["イチゴ"] = 350
print(fruit)

# 辞書の結合
x = {"A": 1, "B": 2}
y = {"C": 3, "D": 4}
z = {"E": 5, "F": 6}
# updateを使う
x.update(y)
print(x)
# ｜を使う (python version 3.9以上で使えます)
w = x | z
print(w)

# 要素数の取得
fruit_len = len(fruit)
print(fruit_len)
