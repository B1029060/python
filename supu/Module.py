# モジュール．パッケージについて

# モジュールとは？
# スクリプトファイルのこと
# そこにクラスや関数が定義されていて、外から使えるようになっています
# ソースコードの部品みたいなものです

# パッケージとは？
# 沢山のモジュールが存在するディレクトリのこと

# ライブラリとは？
# 沢山のパッケージが存在するディレクトリのこと

# モジュールの使い方

import os

current_dir = os.getcwd()    # 作業ディレクトリを取得
result = os.listdir(current_dir)    # ファイルをリストで取得
print(current_dir)
print(result)

import math

result = math.sqrt(2)
print(result)

# パッケージインストール
# pip install パッケージ名
# pip uninstall パッケージ名

import numpy as np

x = np.array([1, 2, 3])
y = np.array([10, 11, 12])
print(x + y)