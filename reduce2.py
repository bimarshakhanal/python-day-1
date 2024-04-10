'''[reduce] Implement a function called concatenate_strings that
takes a list of strings as input and uses the reduce function to
return a single string containing the concatenation of all the elements.'''

from functools import reduce

def concatenate_strings(strings):
    '''Function to calculate factorial of a number'''
    return reduce(lambda x, y: x + y, strings)

if __name__=="__main__":
    strings = input("Enter strings: ").split()
    print("Concatenated String: ",concatenate_strings(strings))
