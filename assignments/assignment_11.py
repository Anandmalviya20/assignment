#test whether a passed letter is a vowel or not

letter = input("Enter a word: ") # Asking the user to enter a word


first = letter[0].lower()  # Converting the first letter to lowercase for comparison


if first in "aeiou":       # Checking if the first letter is a vowel
    print("This letter is a vowel.")
else:
    print("This letter is not a vowel.")
    
