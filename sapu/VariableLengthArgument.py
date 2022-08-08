# 可変長引数について
# 可変長引数とは、関数の引数の数が固定じゃなくて、自由な数だけ設定できる引数のこと
# 引数が一つのタプルに
# 他の引数が前にいる時、値だけで代入。後ろに居る時、変数名に値を指定して書く必要があります。
def func_1(*args, x):
    result = ','.join(args)
    print(f'{x}:{result}')

func_1('あ', x=1)
func_1('あ', 'A', 'a', x=2)
for y in range(1, 6):
    func_1('a', x=y)

# 辞書で受け取る可変長引数
# 他の引数は先に書く必要があります
def func_2(x, **kwargs):
    print(f'{x}:{kwargs}')
func_2(1, name='牛乳', price='300円')
