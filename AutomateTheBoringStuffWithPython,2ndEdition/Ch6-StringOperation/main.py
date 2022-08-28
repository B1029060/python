spam = 'Hello'
print(spam.upper(), spam.lower())
print(spam.upper().isupper(), spam.lower().islower())   # True True
chr1 = 'AbCd'
chr2 = '245'
chr3 = '  '
print(chr1.isalpha(), chr1.isalnum(), chr2.isalnum(), chr2.isdecimal(), chr3.isspace()) # True True True True True

print(chr1.startswith('Ab'), chr3.endswith(' '))    # True True
name_list = ['My', 'name', 'is', 'Simon']
print((name := ' '.join(name_list)))  # My name is Simon
print(name.split()) # ['My', 'name', 'is', 'Simon']
print(name.partition('i'))  # ('My name ', 'i', 's Simon')
print(name.partition('4'))  # ('My name is Simon', '', '')
print('Hello'.ljust(20, '.'))    # 'Hello...............'
print('Hello'.rjust(20))    # '               Hello'
print('Hello'.center(20, '='))   # '=======Hello========'

spam = '  Hello  '
print('|' + spam.strip() + '|' + spam.lstrip() + '|' + spam.rstrip() + '|') # Remove space

# Copy string
import pyperclip    # pip install pyperclip
pyperclip.copy(name)
print(pyperclip.paste())    # My name is Simon

word = 'SpamSpamBaconSpamEggsSpamSpam'
print(word.strip('pSam'))   # BaconSpamEggs/No order/Start from both sides, end when condition is false
