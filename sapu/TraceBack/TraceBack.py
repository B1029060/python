# トレースバックについて
import traceback

try:
    result = 1/0
    print(result)
except ZeroDivisionError:
    print('トレースバック出力開始')
    t = traceback.format_exc()
    print(t)
    print('トレースバック出力終了')
