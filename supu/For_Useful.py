# for文で使うと便利な関数について
# tqdm, zip, enumerate

# tqdm
# for文などの繰り返し処理で進捗を表すプログレスバーを表示する関数
# pip install tqdm

from tqdm import tqdm
for i in tqdm(range(10**7)):
    x = i+1
    # 15秒かかりました

# zip
# 複数の繰り返しオブジェクトから1つずつ順番に要素を取り出して1つにまとめる関数

sales_2020 = [4000, 5000, 6000]
sales_2021 = [5000, 6000, 7000]
for c, p in zip(sales_2021, sales_2020):
    g = ( (c/p) - 1) * 100
    print(f'{g:.2f}%')

# enumerate
# 繰り返しオブジェクトの要素をそのカウントのタプルを要素に持つオブジェクトを作る関数

names = ['A', 'B', 'C']
for idx, value in enumerate(names, start = 1):  # スタートカウント値の設定
    print(f'{value}さん: {idx}位')

