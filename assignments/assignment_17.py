'''
In Python, sequences have both positive and negative indexes:

Positive indexing -starts from 0 and goes towards the right.
Negative indexing -starts from -1 and goes towards the left.
example-'''
my_list = [10, 20, 30, 40, 50]

''' Positive indexes:
            my_list[0] → 10
            my_list[1] → 20
            my_list[2] → 30
    Negative indexes:
            my_list[-1] → 50 (last element)
            my_list[-2] → 40 (second-to-last element)
            my_list[-3] → 30 (third-to-last element)
'''            

'''Why are Negative Indexes Used?
    1)Convenience for Accessing the End'''
#ex
print(my_list[-1])  # Accesses the last element
''' 2)Avoiding Length Calculation:
'''
print(my_list[len(my_list) - 1])  # Access last element using positive indexing
print(my_list[-1]) # Access last element using negative indexing
''' 3)Simplifies Reversing and Slicing:
'''
print(my_list[-3:])  # Slices the last three elements [30, 40, 50]
print(my_list[::-1]) # reversing

          