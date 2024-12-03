'''64) Write a Python function that checks whether a passed string is palindrome or not''' 
# define Function for check palindrome
def check_palindrome(string):
    
    cleaned_str = str.replace(" ", "").lower()  # Replace spaces and convert to lowercase
    
    # Compare the cleaned string with its reverse
    if cleaned_str == cleaned_str[::-1]:  # Check if string is equal to its reverse
        status = True  
    else:
        status = False  
    
    return status  # Return the status (True or False)

# Prompt the user to input a sentence
str = input("Enter sentence: ")

# Check if the entered sentence is a palindrome and print the appropriate message
if check_palindrome(str) is True:
    print(f"Given text is a palindrome")  # If it's a palindrome, print this message
else:
    print(f"Given text is not a palindrome")  # If it's not a palindrome, print this message
