# データクラスについて

# データクラスとは、Python3.7から導入されたクラスで、データの格納するのに特化したクラス
from dataclasses import  dataclass, field

@dataclass    # @で何かを修飾ことをデコレーターと呼ぶ/データクラスは自動的にイニシャライザーを生成
class User:
    name: str
    age: int = 19   # デフォルト値のある変数は後ろに書く

u = User('Kani')
print(u)
@dataclass(frozen=True) # frozen: 値を一度指定したら変更できなくなる
class Items:
    items: list[str] = field(default_factory=list)  # list, set, dict
    nums: list[int] = field(default_factory=lambda: [1, 2, 3])  # デフォルト設定
list_i = ['A', 'B', 'C']
i = Items(list_i)
print(i.items)
print(i.nums)

# フィールド値の一致
class Age:
    def __init__(self, age):
        self.Age = age

@dataclass
class Name:
    name: str

t1 = Age(19)
t2 = Age(19)
print(t1 == t2) # False
s1 = Name('supu')
s2 = Name('supu')
print(s1 == s2) # True

# asdictで辞書に変換
import dataclasses
result = dataclasses.asdict(User('Kani'))
print(result)
