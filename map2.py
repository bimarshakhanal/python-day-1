'''[map] Create a function convert_to_uppercase that takes a list
of strings as input and uses the map function to return a new list
 with all the strings converted to uppercase.'''


def convert_to_uppercase(nums):
    '''Function to convert list of strings to uppercase'''
    return list(map(lambda s: s.upper(), nums))


if __name__ == "__main__":
    strings = input("Enter strings: ").split()
    print("List with uppercased strings: ", convert_to_uppercase(strings))
