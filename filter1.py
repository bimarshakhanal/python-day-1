'''
[filter] Implement a function called filter_prime_numbers that
takes a list of integers as input and uses the filter function to
return a new list containing only the prime numbers.
'''

def check_prime(num):
    '''Function to check if the given number is prime.'''
    if num<2:return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def filter_prime_numbers(nums):
    '''Function to filter prime numbers in list'''
    return list(filter(check_prime,nums))

if __name__=="__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Filtered prime numbers: ",filter_prime_numbers(nums))
