# Python program to get the Fibonacci series of given range. 
f1 = 0        # Start with the first two numbers in the Fibonacci sequence
f2 = 1
num = int(input("Enter a number: ")) ## Take input number  from the user to determine how many Fibonacci numbers to generate
for i in range (0,num):               # Loop through to generate the Fibonacci numbers
    f3 = f1 + f2                     ## Find the next number by adding the two previous ones
    next = f3                         # Save this new number
    f1=f2                             # Move the values forward for the next loop
    f2=f3 
    print(next,end=" ")               # Print the next number, without starting a new line




    
     
    




     