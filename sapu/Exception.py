# 例外処理
# 例外処理とはエラー（例外）への対処
# try-error
x = 1
y = 2

try:
    result = x / y
except ZeroDivisionError as e:
    print("ゼロでは割り切れません")
    print(e)
except NameError as e:
    print("変数が定義されていません")
    print(e)
else:
    print(result)
    print("正常に終了しました")
finally:
    print("割り算が終了しました")

a = 1

try:
    result = a / b
except Exception as e:
    print("例外が発生しました　")
    print(e)

# 外部とデータをやり取りする部分に例外処理を書く　例：ファイルの読み書き、データベースの読み書きなど