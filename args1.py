'''Program to fin sum of multiple numbers'''


def sum_n(*args):
    '''Function to find sum of multiple numbers'''
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Sum is: ", sum_n(*nums))
