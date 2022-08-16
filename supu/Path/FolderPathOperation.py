# フォルダ・パス操作について
# パス(path)とは位置関係のようなものです
# 相対パスのイメージは地図から見て、AのところでBに行きたい行動を執行する時、AからBまでの路径のこと
# 絶対パスはフルパス、なになに県のなになに市にある…のように詳細に書くアドレスのこと

# パス操作の三つのモジュール：os, glob, pathlib(抽象度が一番高い)、今回はpathlibを中心に動く
# pathlib
from  pathlib import  Path
path_c = Path.cwd() # カレントディレクトリのパスを取得
print(path_c)
Dir1 = path_c / 'Dir1'    # パスの結合
print(Dir1)

Dir1_g = Dir1.iterdir() # ジェネレーター(一回しか使用できません)
for x in Dir1_g:
    print(x)    # パス表示
    print(x.name, x.is_file(), x.is_dir(), x.exists())   # ファイルやフォルダの名前のみ表示/ファイルか/ディレクトリか/存在しているか
# Dir1_g内のものが消失

Dir1_g = Dir1.iterdir()    # もう一度生成する
paths = [str(x) for x in Dir1_g]   # stringに転換してからのリスト内包表記、内容が保存された/これでDir1_gの内容消失
print(paths)
print(paths[0])

# pathlibのメリット：簡潔に一行で書くところ
files = [x.name for x in (Path.cwd() / 'Dir1').iterdir()]
print(files)

# 再帰的取得：自分自身を呼び出す(さらにその下にあるファイルやディレクトリまで取得)
Dir1_gall = Dir1.glob(pattern='**/[D]*')  # '(**：再帰的操作)/(*：0文字以上の文字列, ?：任意の一文字, []：特定の一文字)'
Dir1_gtxt = Dir1.glob('**/*.txt')
print('------')
for x in Dir1_gall:
    print(x)
print('------')
for x in Dir1_gtxt:
    print(x.name)
print('------')

# ファイルの作成、削除
Dir2 = Path.cwd() / 'Dir1' / 'Dir2'
for i in range(ord('a'), ord('f')):
    (Dir2 / f'test-{chr(i)}.txt').touch(exist_ok=True)  # ファイル生成/ファイルが既に居てもエラーにならない
(Dir2 / 'test-a.txt').unlink(missing_ok=True)   # ファイル削除/ファイルが存在しなくてもエラーにならない
# ディレクトリの作成、削除
for i in range(1, 11):
    (x := (Path.cwd() / f'NewDir{i}')).mkdir(exist_ok=True)   # NewDir1から10まで作成/エラーにならない
    (x / f'NewTex{i}.txt').touch(exist_ok=True) if i != 5 else None # NewDir5以外にファイル生成しない
(Path.cwd() / 'NewDir5').rmdir()    # 空ディレクトリ削除
