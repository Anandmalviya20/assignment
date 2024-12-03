# 52)How Do You Check the Presence of a Key in A Dictionary?
#1.---------------- Using the in operator---------------------
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Check if the key 'age' exists
if 'age' in my_dict:
    print("Key 'age' is present.")
else:
    print("Key 'age' is not present.")

# Check if the key 'gender' exists
if 'gender' in my_dict.keys():
    print("Key 'gender' is present.")
else:
    print("Key 'gender' is not present.")

#2.------------------ Using the get() method -------------------
value = my_dict.get('age')
if value is not None:
    print("Key 'age' is present with value:", value)
else:
    print("Key 'age' is not present.")  
     

