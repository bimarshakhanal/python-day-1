'''Program to check and group anagrams'''
from collections import defaultdict


def group_anagrams(strings):
    '''Function to return list of anagrams from 
    given list of strings'''

    default_dict = defaultdict(list)
    for string in strings:
        default_dict["".join(sorted(string))].append(string)
    return list(default_dict.values())


if __name__ == "__main__":
    words = input("Enter words: ").split()
    print("Grouped Anagrams: ", group_anagrams(words))
