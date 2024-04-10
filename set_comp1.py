'''
[set comprehension] Given a list of numbers, create a set using
set comprehension that contains only unique even numbers.
'''

def unique_even(nums):
    '''Function to create set of unique even numbers'''

    return {num for num in nums if num%2==0 }

if __name__=="__main__":
    #define dictionary for student records
    nums = list(map(int, input("Enter numbers: ").split()))

    print("Set of unique even numbers: ",unique_even(nums))
