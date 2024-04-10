'''
    [list comprehension] Given three lists list1, list2, and list3,
    each containing integers, write a Python program using list 
    comprehension to generate a new list of unique triplets
    (x, y, z) where x is from list1, y is from list2, and z is from list3,
    such that x + y + z = 0.
'''

def make_triplets(nums1, nums2,nums3):
    '''Function to create list of triplets with a element from each list.'''

    return [(num1,num2,num3) for num1,num2,num3 in zip(nums1,nums2,nums3)]

if __name__=="__main__":
    #Read user input
    nums1 = list(map(int, input("Enter list1: ").split()))
    nums2 = list(map(int, input("Enter list2: ").split()))
    nums3 = list(map(int, input("Enter list2: ").split()))

    if len(nums1) != len(nums2) != len(nums3):
        print("All list should be of same length.")
    else:
        print("Resulting list: ",make_triplets(nums1,nums2,nums3))
