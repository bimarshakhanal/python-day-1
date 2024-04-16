'''
[set comprehension] Given two strings, write a Python program to
create a set using set comprehension that contains all the
characters that are common in both strings.
'''


def common_chars(str1, str2):
    '''Function to create set of unique and common characters of two words'''
    print(str1, str2)
    return set(char for char in str1 if char in str2)


if __name__ == "__main__":
    # define dictionary for student records
    str1 = input("Enter word1: ")
    str2 = input("Enter word2: ")

    print("Set of common chars: ", common_chars(str1, str2))
