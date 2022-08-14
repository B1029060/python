# 日付、時間操作について

wd = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
# 今日の日付を取得
from datetime import date
print(date.today())

# dateオブジェクト
t = date(2022, 8, 1)    # dateの指定
print(t)
print(str(t.year) + '-' +  f'{t.month:002}' + '-' +  f'{t.day:002}')    # int型/ゼロ埋め
print(f'{str(t.month):002}')    # 対照組(str型だとゼロ埋めがstrの後から埋めます)
print(t.weekday())  # 0：月曜日/0-6: 月曜日-日曜日
print(wd[t.weekday()])  # 曜日に転換
# timeオブジェクト
from datetime import time   # デフォルト：(0, 0, 0, 0)/time(時, 分, 秒, マイクロ秒)
u = time(19, 30, 0, 0)  # timeの指定
print(u)    # u.hour, u.minute, u.second, u.microsecond: int型

# datetimeオブジェクト
from datetime import datetime   # dateオブジェクトとtimeオブジェクトのすべての要素を持っている
n = datetime.now()  # 今のdateとtimeを取得
print(n.strftime('%Y-%m-%d %H:%M:%S'), wd[n.weekday()]) # 時間のフォーマット指定
e = datetime(2022, 8, 3, 20, 0, 0, 0)   # datetimeの指定
print(e, wd[e.weekday()])
# timedeltaオブジェクト
from datetime import timedelta
result_1 = datetime(2022, 10, 10) - datetime(2022, 8, 8)
result_2 = datetime(2022, 1, 1, 16) - datetime(2022, 1, 1, 15)
print(result_1.total_seconds()) # 日付まで扱う
print(result_1.days)
print(result_1.total_seconds() / 86400)
print(result_2.seconds)   # hourまでの数値を扱う
new_dt = date(2022, 1, 1) + timedelta(days=1) # 一日進めた状態になります
print(new_dt)
# タイムゾーン
from datetime import timezone
CST = timezone(timedelta(hours=+8)) # Taiwan's timezone
JST = timezone(timedelta(hours=+9)) # Japan's timezone
result = datetime(2022, 8, 7, 20, 16, 30, tzinfo=CST)
print(result)

# 日本の祝日
# pip install jpholiday
import jpholiday
d = datetime(2022, 8, 6)
print(jpholiday.is_holiday(d))  # True:祝日, False:祝日じゃない
print(jpholiday.year_holidays(2022))    # その年にあるすべての祝日を調べる
print(jpholiday.is_holiday_name(datetime(2022, 2, 23))) # その日の祝日の名前を調べる

# 曜日
import locale
dt = datetime(2022, 8, 7)
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')  # 地域を設定して、地域ごとに表示する曜日を変更
print(dt.strftime('%A, %a, %B, %b'))    # 曜日フォーマット(日曜日, 日, 8月, 8)
print(dt.strftime('%Y-%m-%d %H:%M:%S %A'))  # 時間と曜日の組み合わせ
