# while, break, continueについて
x = 0
while x <= 10:
    if x == 10:
        break   # 繰り返し処理を抜ける
    x += 1
    if x % 2 == 1:
        continue    # 後続処理を飛ばす
    print(x)

# whileの使用例
# ファイル読み込み
with open('test_FileOperation4.txt', 'r') as f:
    t = f.readline()
    while t != '':
        print(t)
        t = f.readline()
