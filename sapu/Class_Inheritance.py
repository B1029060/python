# クラスの継承について

# 基底クラス(親クラス、スーパークラス)の性質を派生クラス(子クラス、サブクラス)が引き継ぐ
# 基底クラスの関数とインスタンスを派生クラスの中や宣告された変数からアクセスできます
# 基底クラスのイニシャライザを呼び出す時、super().__init__()と書きます
# 派生クラスのイニシャライザがない時、基底クラスのが呼び出されます
# 多重継承する場合、先の基底クラスが優先します
# 派生クラスが基底クラスと同じ名前の関数を書くことをオーバーライドと言います

# Mixin:インスタンス変数を持たない他のクラスと合わせて使う
# data class:データ格納用のクラス(3.7以降)

class HumanClass:
    def __init__(self):
        print("HumanClassのinit")
        self.hp = 100
    def defend(self):
        print("防御をしました！")

class WizardClass(HumanClass):  # 継承
    def __init__(self):
        super().__init__()
        print("を継承したWizardClassのinit")
        self.mp = 50
    def output_info(self):
        print(f'現在のHPは{self.hp}で、'  # フォーマットの指定
              , f'現在のMPは{self.mp}です。'
              , sep='\n')   # sepに指定した文字が文字列の間に挟みます
    def cast_spell(self):
        print("呪文を唱える")
class SowrdFighterClass:
    def __init__(self):
        print("SwordFighterClassのinit")
    def attack_with_sword(self):
        print("剣で攻撃をする")
class MagicSwordFighterClass(WizardClass, SowrdFighterClass):
    def defend(self):
        print("バリアで攻撃を防げた！")


wizard = WizardClass()
wizard.defend() # 外部からアクセスできます
wizard.output_info()
msf = MagicSwordFighterClass()  # 先に書いたクラスが優先
msf.cast_spell()
msf.attack_with_sword()
msf.defend()    # オーバーライド
