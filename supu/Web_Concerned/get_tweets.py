# PythonでTwitterのTweetを取得

# 第一段階：API用アカウントを作る(Twitter developer Document)

# 第二段階：bearer tokenを環境変数に設定
# ローカルで環境変数を設定して、Pythonで取得すれば、見られても内容を守れます(Pythonで直接書き込みはNG、バレる可能性大)
# Mac：export BEARER_TOKEN = XXX(さっき取得した値) Windows：set BEARER_TOKEN = XXX(さっき取得した値)

# 第三段階：PythonでTweetを取得する
import requests # リクエストする
import os   # 内部osについての操作
import urllib   # '#'みたいな特殊文字を扱う時使う
import json # 取得したデータを見やすくする

# 環境変数設定が必要
bearer_token = os.environ.get('BEARER_TOKEN')   # バレへんバレへん
headers = {'Authorization': f'Bearer {bearer_token}'}  # Header(メールの件名的な感じ)
shishirobotan_2nd_anniversary = urllib.parse.quote('#獅白ぼたん2周年') # デビュー日：8/14
url = f'https://api.twitter.com/2/tweets/search/recent?query={shishirobotan_2nd_anniversary} -is:retweet'  # このurlにリクエスト投げます
response = requests.get(url, headers=headers)  # Twitter側にリクエスト送って、レスポンスが帰ってくる
# 中身がわからないので、json形式に変換して、Python側ではリストとして扱います
json_response = response.json()
print(json.dumps(json_response, indent=4, ensure_ascii=False))
