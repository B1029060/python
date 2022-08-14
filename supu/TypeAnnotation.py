# タイプアノテーション（型注釈）について
# 関数の引数と戻り値に型を指定
# 戻り値：int, float, List[int], dict, set, tuple, None
# 代入した値の型が違ってもエラーにはならない、あくまで注釈

# 一般の関数
def total_price(unit_price, quantity = 1):  # デフォルト値の設定
    return unit_price * quantity

# タイプアノテーション
def total_price_TA(unit_price: int, quantity:int = 1) -> int:   # 引数と戻り値の型設定
    return unit_price * quantity
def total_price_TA_kanma(unit_price: int, quantity:int = 1) -> str:
    return f'¥{unit_price * quantity: ,}'
p1 = total_price(100, 10)
p2 = total_price_TA(100, 10)
print(p1, p2)
p3 = total_price_TA_kanma(100, 10)
print(p3)
