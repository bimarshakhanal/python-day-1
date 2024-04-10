'''
[filter] Write a Python function filter_long_strings that takes
a list of strings as input and uses the filter function to return
a new list containing strings with more than 5 characters.
'''

def filter_long_strings(strings):
    '''Function to filter prime numbers in list'''
    return list(filter(lambda s: len(s)>5,strings))

if __name__=="__main__":
    strings = input("Enter strings: ").split()
    print("Filtered long strings: ",filter_long_strings(strings))
