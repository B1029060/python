import time, sys
indent = 0
flag = True

try:
    while True:
        print(' ' * indent + '********')
        time.sleep(0.1)

        if flag:
            indent += 1
            flag = False if indent == 20 else True
        else:
            indent -= 1
            flag = True if indent == 0 else False
except KeyboardInterrupt:
    sys.exit()
