'''
    [dictionary comprehension] Given two lists
    one containing keys and another containing values,
    create a dictionary using dictionary comprehension.
'''


def create_dict(list1, list2):
    '''Function to create dictionary using key-value pairs from lists.'''

    return {k: v for k, v in zip(list1, list2)}


if __name__ == "__main__":
    # Read user input
    keys = input("Enter keys list: ").split()
    values = input("Enter values list: ").split()

    if len(keys) != len(values):
        print("Both list should be of same length.")
    else:
        print("Resulting list: ", create_dict(keys, values))
