def concat_strings(*args):
    '''Function to concat multiple strings'''
    concat = ""
    for string in args:
        concat += string
    return concat

if __name__=="__main__":
    strings = input("Input strings: ").split()
    print("Concated string: ",concat_strings(*strings))
