# Python program to swap two numbers using a temporary variable and without using a temporary variable.

# Using a temporary variable:
a = 2  # Initial value of a
b = 5  # Initial value of b
c = a  # Store value of a in c (temporary variable)
a = b  # Assign value of b to a
b = c  # Assign value of c (original a) to b
print(a, b)  # Output the swapped values of a and b

# Without using a temporary variable:
a = 2  # Initial value of a
b = 5  # Initial value of b
b = b - a  # Subtract a from b and store the result in b
a = a + b  # Add the new value of b to a
b = a - b  # Subtract the new value of b from a to get original value of a
print(a, b)  # Output the swapped values of a and b








