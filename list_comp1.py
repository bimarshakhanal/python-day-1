'''[list comprehension] Given a list of strings, create a new
list that contains only the strings with more than 5 characters
using list comprehension.'''

def filter_strings(strings):
    '''Function to filter strings from list of strings using
    list comprehension'''

    return [string for string in strings if len(string)>5]

if __name__=="__main__":
    #Read user input
    strings = input("Enter strings: ").split()
    
    print("Filtered string list: ",filter_strings(strings))
