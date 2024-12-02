#51)How Do You Traverse Through a Dictionary Object in Python?
#1. Traversing Through Keys
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict.keys():
    print(key)

#2.Traversing Through Values
for value in my_dict.values():
    print(value)

#3.Traversing Through Key-Value Pairs
for k,v in my_dict.items():
    print(f"{k}={v}") 


