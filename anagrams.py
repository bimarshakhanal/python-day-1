from collections import defaultdict

def group_anagrams(strings):
    '''Function to return list of anagrams from 
    given list of strings'''
    
    defDict = defaultdict(list)
    for string in strings:
        defDict["".join(sorted(string))].append(string)
    return list(defDict.values())

if __name__=="__main__":
    strings = input("Enter strings: ").split()
    print("Grouped Anagrams: ",group_anagrams(strings))
