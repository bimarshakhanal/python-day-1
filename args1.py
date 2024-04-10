def sumN(*args):
    '''Function to find sum of multiple numbers'''
    sum = 0
    for n in args:
        sum += n
    return sum

if __name__=="__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Sum is: ",sumN(*nums))
