# pip install pyinputplus
import  pyinputplus as pyip

response = pyip.inputYesNo('Enter yes or no:　')
print(response)
response = pyip.inputNum('Please enter number: ', min=1, lessThan=10)    # [1-9], at last 3 times
print(response)
response = pyip.inputNum('Next one: ', max=999, greaterThan=9)  # [10-999]
print(response)
blank = pyip.inputNum('Enter blank: ', blank=True)
print(f'\'{blank}\'')
res = pyip.inputNum('Please enter number in 7 seconds: ', limit=1, default='N/A', timeout=7)  # 1 time, in 7 seconds
print(res if res != 'N/A' else 'Time Out!')
res_roman = pyip.inputNum('Enter Roman number: ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'], blockRegexes=r'[0-9]+')
print(res_roman, type(res_roman))   # XVII <class 'str'>

def AddsUpToTen(num):
    numlist = list(num)
    counter = 0
    for idx, val in enumerate(numlist):
        counter += int(val)
    print(num if counter == 10 else f'The digits must add up to 10, not {counter}')

print('Make sure the digits add up to ten')
res_ten = pyip.inputCustom(AddsUpToTen)    # Define pattern you want
