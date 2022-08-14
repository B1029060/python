# セイウチ演算子について
# Python3.8から導入された

# 代入式
# 変数への代入と評価を1行で書ける構文
l = list(range(10))
print(f'要素：　{l}\n数： {len(l)}')
if (n := len(l)) >= 10: # セイウチ演算子(セイウチっぽく見えるため)
    print('このリストは長すぎます')
# whileでのファイル読み込み
with open('test_FileOperation.txt') as f:
    while (r := f.readline()) != '':
        print(r)

# 正規表現でマッチする部分を抽出
import re
s = '合計金額は1200円です'
if (m := re.search(r'[0-9]+円', s)):
    print(m.group())
