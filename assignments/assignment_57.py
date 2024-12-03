#57) Write a Python program to find the highest 3 values in a dictionary.

dic = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1} # Define a dictionary with fruit names as keys and quantities as values

items = dic.items() # Get the dictionary's items as a list of tuples (key, value)

# Sort the items by the value (second element of the tuple) in descending order
# Use lambda to extract the second element (value) for sorting
# After sorting, slice the first three items ([:3]) to get the top 3 highest values
sort_dict = dict(sorted(items, key=lambda items: items[1], reverse=True)[:3])


print(sort_dict) # Print the sorted dictionary with the top 3 items
