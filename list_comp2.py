'''
[list comprehension] Given two lists of integers, create a list
that contains the product of each element of the first list with
the corresponding element in the second list using list comprehension.
'''


def list_product(nums1, nums2):
    '''Function to find elementwise product of two list using
    list comprehension'''

    return [num1*num2 for num1, num2 in zip(nums1, nums2)]


if __name__ == "__main__":
    # Read user input
    nums1 = list(map(int, input("Enter list1: ").split()))
    nums2 = list(map(int, input("Enter list2: ").split()))

    if len(nums1) != len(nums2):
        print("Both list should be of same length.")
    else:
        print("Resulting list: ", list_product(nums1, nums2))
