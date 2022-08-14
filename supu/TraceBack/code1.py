import  traceback
import code2
from logging import getLogger, FileHandler, DEBUG, Formatter
formatter = Formatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
logger = getLogger(__name__)
handler = FileHandler('test_log.txt')
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)

def main():
    try:
        code2.func1()
    except Exception:
        t = traceback.format_exc()
        logger.debug(t)
        '''
        # 他のファイルに入力したい時
        with open('../test_Logging.txt', 'a') as f:
            traceback.print_exc(file=f)
        '''
if __name__ == '__main__':
    main()
