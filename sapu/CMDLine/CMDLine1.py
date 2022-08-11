# コマンドライン引数について
# 位置引数
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # ArgumentParserオブジェクトの生成
    parser.add_argument('language', choices=['English', 'Japanese'])    # 言語選択
    parser.add_argument('numbers', help='掛け算を行う', type=int, nargs=3)   # 引数名を追加/いくつの値を受け取るのか
    args = parser.parse_args()  # 渡されたコマンドライン引数を取得
    print(args.numbers[0] * args.numbers[1] * args.numbers[2])  # 対応している引数の値を表示する
# python xxxx.py 'value'
