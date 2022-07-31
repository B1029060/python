# ラムダ式について
#　関数オブジェクトを作る方法で、名前を付けるほどではない小さい関数を使う時に使う
# ラムダ式で作った関数オブジェクトをムメイ関数と言う
# PEP8では非推奨

func = lambda x:print(f'{x}!')
func("Hi")

# ラムダ式は他の関数と組み合わせて使う(map, filter...)

# map関数は繰り返しオブジェクトのすべての要素にある処理を行う関数
num = [1, 2, 3]
new_num = list(map(lambda i: i - 1, num))   # map(関数, 繰り返しオブジェクト)
print(new_num)

# filter関数は繰り返しオブジェクトの中である条件がTrueになる要素だけを抽選する関数
cnt = [x for x in range(30)]
new_cnt = list(filter(lambda x: x>=20, cnt))    # filter(関数, 繰り返しオブジェクト)
print(new_cnt)

# ラムダ式の使用はリストに限らない
