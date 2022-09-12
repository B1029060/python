X, Y, N = map(int, input().split())
def buyApple(price_1, price_3, quantity):
    if price_3 / 3 >= price_1:
        return price_1 * quantity
    elif price_3 / 3 < price_1:
        total_price = int(quantity / 3) * price_3 + (quantity % 3) * price_1
        return total_price
print((totl := buyApple(X, Y, N)))
