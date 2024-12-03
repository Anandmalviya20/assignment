'''Write a Python function to calculate the factorial of a number (a 
nonnegative integer) '''
def find_factorial(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    print(fact) 
num=5
find_factorial(num)       
