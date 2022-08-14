# オプショナル引数
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', default='text')   # 省略名/正式名
    args = parser.parse_args()
    print(args.text)
# python xxx.py -t 'value'
