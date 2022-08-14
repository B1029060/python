# About this function
# if num is odd, return 3 * num + 1, if num was even, then return num / 2

def Collatz(num):
    if num >= 2 and num != 1:
        print((new_num := int(3 * num + 1))) if num % 2 == 1 else print((new_num := int(num / 2)))
        Collatz(new_num)    # Recursive
    elif num != 1:
        print('Invalid input')  # print 'Invalid input' when num is integer under 1

try:
    print('Enter number: ')
    Collatz(int(input()))   # assign int variable type
except ValueError:
    print('Wrong Variable Type')
    print('Please input right variable type: int')
except RecursionError:
    print('Infinit Recursion happened!')
finally:
    print('Program Finished')
