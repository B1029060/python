spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(list):
    if len(list) == 0:
        return 0
    for x in range(len(list)):
        print(list[x], end=', ')
        if x == len(list) - 2:
            print(f'and {list[x + 1]}')
            break

comma(spam) # apples, bananas, tofu, and cats

