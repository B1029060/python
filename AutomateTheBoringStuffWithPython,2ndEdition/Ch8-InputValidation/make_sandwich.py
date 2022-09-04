# Make your own sandwich!!
import pyinputplus as pyin

price = 0
quantity = 0
menuBread = {'wheat': 30, 'white': 40, 'sourdough': 35}
menuProtein = {'chicken': 35, 'turkey': 45, 'ham': 30, 'tofu': 25}
addServing = {'mayo': 10, 'mustard': 10, 'lettuce': 10, 'tomato': 10}
addCheese = {'cheddar': 15, 'Swiss': 20, 'mozzarella': 15}
check = []
step1 = pyin.inputMenu(list(menuBread.keys()), prompt='Which bread type do you choice?\n', numbered=True)
check.append((s1 := step1 + ': ' + str(menuBread[step1])))
print(s1)
price += menuBread[step1]
step2 = pyin.inputMenu(list(menuProtein.keys()), prompt='Which protein do you choice?\n', numbered=True)
check.append((s2 := step2 + ': ' + str(menuProtein[step2])))
print(s2)
price += menuProtein[step2]
askServing = pyin.inputYesNo(prompt='Do you want add serving?\n')
if askServing == 'yes':
    step3 = pyin.inputMenu(list(addServing.keys()), prompt='Which serving do you choice?\n', numbered=True)
    check.append((s3 := step3 + ': ' + str(addServing[step3])))
    print(s3)
    price += addServing[step3]
askCheese = pyin.inputYesNo(prompt='Do you want add cheese?\n')
if askCheese == 'yes':
    step4 = pyin.inputMenu(list(addCheese.keys()), prompt='Which cheese do you choice?\n', numbered=True)
    check.append((s4 := step4 + ': ' + str(addCheese[step4])))
    print(s4)
    price += addCheese[step4]
step5 = pyin.inputNum(min=1, max=12, prompt='How many do you buy?\n')
check.append((s5 := 'Amount: ' + str(step5)))
print(s5)
price *= step5
print(check)
print('Total price: ' + str(price))