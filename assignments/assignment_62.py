'''Write a Python function to check whether a number is in a given range 
'''
# Function to check if the number is within the range 1 to 100 (inclusive)
def check_number(number):
    
    if 1 <= number <= 100:  # Directly check if the number is in the range from 1 to 100
        return True  # If the number is in the range, return True
    else:
        return False  # If the number is not in the range, return False        

# Ask the user to input a number, and convert it to an integer
number = int(input("Enter a number: "))

# Call the check_number function with the input number and print the result
print(check_number(number))


