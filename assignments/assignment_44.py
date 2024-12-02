#Write a Python program to unzip a list of tuples into individual lists.
# List of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzip the list of tuples into individual lists
list1, list2 = zip(*list_of_tuples)

# Convert the result into lists (since zip returns a tuple)
list1 = list(list1)
list2 = list(list2)

# Print the individual lists
print("List 1:", list1)
print("List 2:", list2)
