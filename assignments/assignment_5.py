'''Python program to get the Factorial number of given numbers. ''' 
fact=1      # Initialize a variable 'fact' to 1, which will store the factorial result   
num =int(input("enter number: ")) # Ask the user to input a number and convert it to an integer

for i in range (num,0,-1): # Loop from the value of 'num' down to 1 (inclusive) in steps of -1
    fact*=i    # Multiply 'fact' by the current value of 'i' in each iteration
print(f"{num}! is equals to = {fact}") # Print the final factorial result    
    
     



