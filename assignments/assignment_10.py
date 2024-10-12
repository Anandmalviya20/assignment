#find whether a given number is even or odd, print out an appropriate message to the user.
# Ask the user to enter a number and store it as an integer in the variable 'num'
num = int(input("enter number: "))

# Check if the number is divisible by 2 (i.e., if it is even)
if num % 2 == 0:
    # If the number is even, print that it is even
    print(f"{num} is even")
else:
    # If the number is not divisible by 2 (i.e., it's odd), print that it is odd
    print(f"{num} is odd")
       