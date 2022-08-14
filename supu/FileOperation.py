# ファイル操作について
# 今回はテキストファイルを対象とします
# open("ファイル名", モード)
# ディレクトリのデフォルト：作業中のファイルのディレクトリ
# モードのデフォルト：r(読み込みのみ)

# ファイルオープン

# 他のディレクトリのファイルを開ける時
# ".."で一つ前のディレクトリに戻ります、　"/ファイル名"で指定したファイルに入る
with open("../AtCoder/BeginnerContest/261/A_Intersection.py") as f:
    s = f.read()
    print(s)
# with内のコードが全部実行されたら、自動的に閉じる(クローズ)

# デフォルトのディレクトリ内のファイル
with open("test_FileOperation.txt") as f:
    s = f.read()    # 内容を読み込む
    print(s)
with open("test_FileOperation.txt") as f:
    for _ in range(2):
        s_line = f.readline()    # 一行ずつ読み込む
        print(s_line)
with open("test_FileOperation.txt") as f:
    for _ in range(4):
        s_line = f.readline()
        print(s_line)
        if s_line == "":    # 空だった場合、''や""で表記できます
            print("終了です")
with open("test_FileOperation.txt") as f:
    s_line = f.readlines()    # すべての行をリストで取得する
    print(s_line)
# モードが"w"で、ファイルが存在しない場合、新しく作ります
# encoding="UTF-8"で文字化けをなくします
with open("test_FileOperation2.txt", 'w', encoding="UTF-8") as f:
    f.write("あああ\nいいい\nううう")
with open("test_FileOperation2.txt", 'a', encoding="UTF-8") as f:
    f.write("\nえええ\nおおお")
x_list = ["apple", "orange", "banana"]
with open("test_FileOperation3.txt", 'w') as f:
    # リストの中身を一列に書き込む
    f.writelines(x_list)    # リストであるため、f.writelines()を使う
s = '\n'.join(x_list)   # 要素の後ろに'\n'を追加して、全要素を取得した"文字列"になる
with open("test_FileOperation4.txt", 'w') as f:
    f.write(s)  # 文字列であるため、f.write()を使う
