'''
69) How will you set the starting value in generating random numbers?
'''
import random

random.seed(1)
print(random.randint(1, 100))  # Always gives the same result for the same seed

