'''
66) How can you pick a random item from a list or tuple? 
'''
import random

my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)
print(random_item)

my_tuple =("banana","mango","orange")
random_ite=random.choice(my_tuple)
print(random_ite)