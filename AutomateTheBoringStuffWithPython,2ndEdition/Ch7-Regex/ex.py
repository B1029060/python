# Find number cut in three for a pair by comma e.g. 1,234,567、24、4,555
import re
def find_comma(obj):
    dt = re.compile(r'\d{1,3}(,\d{3})*')
    result = dt.search(obj)
    if result.group() == obj:
        print(result.group())
    else:
        print(f'\'{obj}\' is not a regular number')

num = '23,456,789'
fake_num = '23,45,67'
find_comma(num) # 23,456,789
find_comma(fake_num)    # "23,45,67" is not a regular number

# Find name Watanabe
def find_Watanabe(name):
    dt = re.compile(r'([A-Z]{1}[a-z]+\sWatanabe)')
    result = dt.search(name)
    if result:
        print(result.group())
    else:
        print(f'{name} is not a real Watanabe')

person_1 = 'Satoshi Watanabe'
person_2 = 'Robocop Watanabe'
person_3 = 'Mr. Watanabe'
person_4 = 'satoshi Watanabe'

find_Watanabe(person_1) # Satoshi Watanabe
find_Watanabe(person_2) # Robocop Watanabe
find_Watanabe(person_3) # Mr. Watanabe is not a real Watanabe
find_Watanabe(person_4) # satoshi Watanabe is not a real Watanabe

# Compare sentence
def compare_sentence(sentence):
    dt = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.')
    result = dt.search(sentence)
    if result:
        print(result.group())
    else:
        print('Irregular sentence: ' + sentence)

stc_1 = 'Alice pets cats.'
stc_2 = 'Alice is beautiful'
compare_sentence(stc_1)
compare_sentence(stc_2)
