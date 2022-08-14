# ログ出力の基本について
# プログラムを使う人に向けたメッセージ
# 1.問題が起きた時に原因を突き止め解決する
# 2.想定した通りのうごきをしているか確認する

from logging import getLogger, StreamHandler, DEBUG
# ログレベル：DEBUG, INFO, WARNING, ERROR, CRITICAL
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG) # これ以上のログレベルを扱う、以下は扱わない
logger.setLevel(DEBUG)  # 同上
logger.addHandler(handler)
logger.debug("これはデバッグログです") # Logger -> Handler -> Logger.ログレベル()

# ログの出力形式：時間、レベル、ファイル
from logging import Formatter, FileHandler
# ログのフォーマット
# ログレベル：　'%(levelname)s'
# 時間：　'%(asctime)s'
# メッセージ：　'%(message)s'
# ファイル名：　'%(filename)s'
formatter = Formatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
logger_f = getLogger(__name__)
handler_f = FileHandler("test_Logging.txt", encoding="UTF-8")   # 文字をUTF-8に指定
handler_f.setLevel(DEBUG)
handler_f.setFormatter(formatter)
logger_f.setLevel(DEBUG)
logger_f.addHandler(handler_f)
logger_f.debug("ファイルがある")

