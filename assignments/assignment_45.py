#Write a Python program to convert a list of tuples into a dictionary.
lis =[("a",1),("b",2),("c",3)] #list of tuples
dictionary ={}                 #initialize blank dictionary

for key, value in lis:         #Iterate through each tuple in the list 
    dictionary[key]= value     #Add the tuple as a key-value pair in the dictionary
print(dictionary)              #print the dictinary
