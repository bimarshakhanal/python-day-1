'''
[map] Write a Python function square_numbers that takes a list
of integers as input and uses the map function to return a new
list containing the square of each element.
'''

def square_numbers(nums):
    '''Function to find square of numbers in list'''
    return list(map(lambda x: x*x, nums))

if __name__=="__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("List with squared numbers: ",square_numbers(nums))
