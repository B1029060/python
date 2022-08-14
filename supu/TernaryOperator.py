# 三項演算子について

# 条件の結果によって返す値を変えることができる算子
# if文との違い：値は必ず返す、if...else...の形だけ
# 特徴：スッキリ書ける、読みやすい
# elifをネストで表現できる

age = 20
result = "成人" if age >= 20 else "子ども" if age >= 1 else "赤ちゃん"
# "値 if 条件"　でひとつのif文として見なす
# "else 値"　でelseと見なす
# "else 値　if 条件"　でelifと見なす
print(result)