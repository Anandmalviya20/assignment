# Program to calculate the sum of three given integers.
# If two values are equal, the sum will be zero.

num1 = int(input("Enter number: "))  # Taking the first number as input from the user
num2 = int(input("Enter number: "))  # Taking the second number as input from the user
num3 = int(input("Enter number: "))  # Taking the third number as input from the user

# Checking if any two of the numbers are equal
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Sum of three values is zero")  # If any two numbers are equal, print zero
else:
    # If none of the numbers are equal, print the sum of the three numbers
    print(f"Sum of three values is {num1 + num2 + num3}")
  