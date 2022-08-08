import Module2  # importした時点でModule2.py内のfunc3()が実行された
import Module3  # mainにいないため、実行しません
def main():
    Module2.func2()
    print('-----')
    Module3.func2()

if __name__ == '__main__':
    main()

from SubModuleFolder import SubModule1
SubModule1.sub_func1()
# Python3.3より前のバージョンでは'__init__.py'が必要
