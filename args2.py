'''Program to joing multiple strings'''


def concat_strings(*args):
    '''Function to concat multiple strings'''
    return "".join(args)


if __name__ == "__main__":
    strings = input("Input strings: ").split()
    print("Concated string: ", concat_strings(*strings))
