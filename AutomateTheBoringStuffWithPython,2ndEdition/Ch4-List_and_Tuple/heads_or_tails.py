# Find the probability of six continuous coins in same side, toss a coin 10000 times to calculate it.
import random
from tqdm import tqdm   # pip install tqdm
list_coin = []
now_coin = ''
for x in tqdm(range(10 ** 7)):
    list_coin.append('T' if (y := random.randint(0, 1)) == 1 else 'H')
    conti_coins = 0
    if now_coin == list_coin[x]:
        conti_coins += 1
    else:
        conti_coins = 1
        now_coin = list_coin[x]
    if conti_coins == 6:
        print(f'{((10 ** 7 - x - 1)/(10 ** 7)):.4f}%')
        break
    elif x == (10 ** 7 - 1):
        print('0%')
# 100%|██████████| 10000000/10000000 [00:10<00:00, 971693.72it/s]
# 0%


