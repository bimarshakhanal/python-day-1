'''
[dictionary comprehension] Create a dictionary using dictionary
comprehension to represent the ASCII values of lowercase alphabets
(a-z) where the keys are the alphabets, and the values are their 
corresponding ASCII values.
'''

def get_ASCII(alphas):
    '''Function to create dictionary of alphabets-ASCII pairs.'''

    return {alpha:ord(alpha) for alpha in alphas }

if __name__=="__main__":
    #read input from user
    alphas = input("Enter alphabets: ").split()
    
    print("Dictionary of ASCII values: ",get_ASCII(alphas))
