import pyinputplus as pyin

counter = 0
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?'
    response = pyin.inputYesNo(prompt)
    if response == 'no':
        print('Thank you, have a nice day.')
        break
    if (counter := counter + 1) == 100:
        print('You are that idiot!!')
        break

'''
try:
    prompt = 'Want to know how to keep an idiot busy for hours?'
    res = pyin.inputYesNo(prompt=prompt, limit=100, blockRegexes=[(r'[Yy]([Ee][Ss])?', '')])
    if res == 'no':
        print('Thank you, have a nice day.')
except pyin.RetryLimitException:
    print('You are that idiot!!')
'''