# リスト内包表記について
# リストを簡単に生成する表記、forで一行に書ける

# 基本
x = [i + 1000 for i in range(6)]
print(x)
names = ["高木", "友利", "那由多"]
x = [i + "さん" for i in names]
print(x)

# 条件付き
x = [i for i in range(10) if i % 2 == 1]
x_c = [2 * i + 1 for i in range(5)] # 対照組
print(x)
print(x_c)

# 三項演算子
city = ["東京", "埼玉", "静岡", "北海道"]
x = [i + '都' if i == "東京" else i + '県' for i in city]
print(x)
