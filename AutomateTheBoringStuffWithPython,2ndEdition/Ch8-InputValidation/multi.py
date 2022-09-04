import pyinputplus as pyin
import random, time

numberOfQuestion = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestion):
    num1, num2 = random.randint(1, 19), random.randint(1, 19)
    prompt = '#%s: %s x %s =  ' %(questionNumber + 1, num1, num2)
    try:
        response = pyin.inputStr(prompt, allowRegexes=['^%s$' %(num1 * num2)], blockRegexes=['.*'], limit=2, timeout=10)
    except pyin.TimeoutException:
        print('Time out!')
    except pyin.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
print('Score: %s / %s' %(correctAnswers, numberOfQuestion))
