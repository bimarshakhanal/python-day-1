'''
[reduce] Write a Python function calculate_factorial that takes
an integer as input and uses the reduce function to return the
factorial of that number.
'''

from functools import reduce


def calculate_factorial(num):
    '''Function to calculate factorial of a number'''
    nums = list(range(1, num+1))
    return reduce(lambda x, y: x * y, nums)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial: ", calculate_factorial(num))
