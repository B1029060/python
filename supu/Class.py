# クラスについて
# クラスは設計図、これでオブジェクト（"インスタント"とも呼ぶ）を作る
# クラスが持ってる関数を"メソッド"と呼びます
# def _init_() は、一回だけ呼ばれる関数です
'''
def _init(self, 引数...）：
    self.変数名 = 引数　
'''

# 実際にコードを動かす
class BodyCondition:
    def __init__(self, arg_weight, arg_height):
        print("初期化")
        self.weight = arg_weight
        self.height = arg_height

    def bmi_calc(self):
        m_height = self.height / 100
        bmi = self.weight / (m_height ** 2)
        print(bmi)

bc = BodyCondition(55, 150)
print(bc.height)
print(bc.weight)
bc.bmi_calc()