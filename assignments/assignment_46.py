#46.How will you create a dictionary using tuples in python? 
# Tuple with alternating keys and values
tup = ("a", 1, "b", 2, "c", 3, "d", 4)

# Initialize an empty dictionary
dic = {}

# Loop through the tuple, picking key-value pairs
for i in range(0, len(tup), 2):
    dic[tup[i]] = tup[i+1]  # Set key-value pair in dictionary

# Print the dictionary
print(dic)

