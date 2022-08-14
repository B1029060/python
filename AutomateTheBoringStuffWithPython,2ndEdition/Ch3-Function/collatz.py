# About this function
# if num is odd, return 3 * num + 1, if num was even, then return num / 2
num_list = []
def collatz(num: int) -> None:  # Type Annotation
    num_list.append(num)
    if num >= 2:
        print((new_num := int(3 * num + 1))) if num % 2 == 1 else print((new_num := int(num / 2)))
        collatz(new_num)    # Recursive
    elif num != 1:
        print('Invalid input')  # print 'Invalid input' when num is integer under 1
    if num == 1:
        print(f'Input number: {num_list[0]}')
        print(f'The collatz sequence: {num_list}')

try:
    print('Enter number: ')
    collatz(int(input()))   # assign int variable type
except ValueError:
    print('Wrong Variable Type')
    print('Please input right variable type: int')
except RecursionError:
    print('Infinite Recursion happened!')
finally:
    print('Program Finished')
