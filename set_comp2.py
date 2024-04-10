'''
[set comprehension] Given a list of words, write a Python program
to create a set using set comprehension that contains all the
unique characters present in the words.
'''

def unique_chars(strings):
    '''Function to create set of unique characters in given words'''

    return {''.join(set(string)) for string in strings}

if __name__=="__main__":
    #define dictionary for student records
    strings = input("Enter strings: ").split()

    print("Set of unique characters: ",unique_chars(strings))
