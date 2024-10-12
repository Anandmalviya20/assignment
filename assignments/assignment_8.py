#What is the purpose continuing statement in python?
'''
* The continue statement in Python is used within loops. 
* It allows you to skip the rest of the current iteration and 
   jump to the next iteration of the loop. 
* Imagine you’re sorting through a stack of papers, and whenever you come across
   a paper you’re not interested in, you just set it aside and move on to the next one without reading the rest.
'''
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
