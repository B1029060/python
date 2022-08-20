# Jsonモジュールについて
# JavaScript Object Notationの略、データフォーマットの一種
# 言語問わずに使用されている、違う言語で保存したデータが扱えるようになっています
# データの供述形式：JSON(Web API)、XML、CSVなど

# Python -> JSON
import json
obj = {'SSRB': '2ndAnni.', 'price': 8500}
json_text = json.dumps(obj)
print(json_text)    # {"SSRB": "2ndAnni.", "price": 8500}
print(type(json_text))  # <class 'str'>

new_obj = {'is_student': True, 'license': None}
json_text = json.dumps(new_obj)
print(json_text)    # {"is_student": true, "license": null}

prime_number_under_ten = {'奇数': [3, 5, 7], '偶数': 2}
json_text = json.dumps(prime_number_under_ten, ensure_ascii=False) # asciiに変換しないで
print(json_text)    # {"奇数": [3, 5, 7], "偶数": 2}

# JSON -> Python
text = '{"id": 446, "is_lion": true}'
obj = json.loads(text)
print(obj)  # {'id': 446, 'is_lion': True}
print(type(obj))    # <class 'dict'>
print(obj['id'])    # 446

text = '{"id": 446, "sub":{"member": 1230000, "vids": 646, "rcd_time": "2022/08/20"}}'
obj = json.loads(text)
print(obj)  # {'id': 446, 'sub': {'member': 1230000, 'vids': 646, 'rcd_time': '2022/08/20'}}
print(obj['sub']['vids'])   # 646

#  特殊文字
obj = {r'it\em': 0, r'ti"me': r'unk\now"n'} # 特殊文字を打つ時、raw文字列にしましょう
json_text = json.dumps(obj)
print(json_text)    # {"it\\em": 0, "ti\"me": "unk\\now\"n"}

text = r'{"ER\\RO\"R": "!@#$%^&*()", "H\"EL\\L\"O": "FROM W\\G@3#4LA*^B"}'
obj = json.loads(text)
print(obj) # {"ER\\RO\"R": {'ER\\RO"R': '!@#$%^&*()', 'H"EL\\L"O': 'FROM W\\G@3#4LA*^B'} # \\が変換されてないように見えますが
print(obj[r'H"EL\L"O']) # FROM W\G@3#4LA*^B # ちゃんと変換されています


