# print 'Hello' when spam = 1, 'Howdy' when spam = 2, 'Greetings!' when else
print('Please enter a number:')
spam = input()
if spam == '1':
    print('Hello')
elif spam == '2':
    print('Howdy')
else:
    print('Greetings!')
'''
spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greeings!')  # It came out to be error when input can't be turned to int like letter, symbol, e.t.c
'''