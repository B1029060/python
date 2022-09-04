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
