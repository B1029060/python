# 正規表現について
# [ab9] => 'a' or 'b' or '9'。[a-z] => 小文字の英字1文字。 [0-9] => 半角数字1文字, [a-zA-Z] => 英字1文字。
# [^] => ある集合以外の1文字, 例：[^0-9] => 半角数字以外の1文字, [^ab9] => 'a', 'b', '9'以外の1文字。
# . => 改行以外の1文字, 例：abc.の場合、abcd, abc0は当てはまります、bbc, abcは当てはまらない。
# ^ => 文字列の先頭, 例：^id[0-9] => idから始まって、数字1文字が続く
# $ => 文字列の末尾, 例：[0-9]point$ => 数字1文字とpointで終わる文字列
# *, +, ? => 直前の文字を　0回以上,1回以上,0/1回だけ　繰り返す
# {n}, {n, m} => 直前の文字を n回, n~m回繰り返す, 例：[a-z]{3, 5} => abc, xyzzzは当てはまります
# | => 左か右のどちらか, 例：[0-9]|[a-z] => 半角数字1文字か小文字の英字1文字

import re   #  正規表現のモジュール
text = '12345678b'
m = re.match(r'[0-9]{3}', text)
print(m)
if m:
    print(m.group())  # 一致している部分を取り出す
    print(m.start())    # 開始インデックス
    print(m.end())  # 終了インデックス
    print(m.span()) # 開始インデックスと終了インデックスを含んだタプル
USD = 'It cost USD900'
m = re.search(r'USD[1-9][0-9]*', USD)
if m:
    print(m.group())
    print(m.span())

m = re.fullmatch(r'[0-9]*', text)   # 文字列全体がマッチするかどうかのマッチオブジェクト
print(m.group()) if m else print('None')    # None
m = re.findall(r'[0-9]{4}', text)   # マッチする部分をリストに記入
print(m)    # ['1234', '5678']

# 特殊な文字を使う時、\を使います、これをエスケープと言います
s = 'a9+9a'
t = 'a9"9a'
u = "a9'9a"
m = re.search(r'[0-9]\+[0-9]', s)
if m:
    print(m.group())    # 9+9
m = re.search(r'[0-9]\"[0-9]', t)
if m:
    print(m.group())    # 9"9
m = re.search(r'[0-9]\'[0-9]', u)
if m:
    print(m.group())    # 9'9

# 他にも
# () => グルーピング。　re.sub => 文字列置換。 re.split => 文字列分割
# 正規表現はどの言語も同じ、検索バーで見れます
