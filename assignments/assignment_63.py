#Write a Python function to check whether a number is perfect or not.
def perfect_check(number):
    divisor_sum=0
    for i in range(1,number):
        if number%i ==0 :
            divisor_sum+=i
        else :
            check= False 
    if divisor_sum==number:
        check= True 
    else:
        check=False
    return check 
number=int(input("enter number : ")) 
if perfect_check(number) is True:
    print(f"{number} is perfect number")
else:
    print(f"{number} is not perfect number")    
              



