#Write a Python program to check whether a list contains a sub list 
main_list = [1, 2, 3, 4, 5]
sublist = [3,4]
for items in sublist:
    if items in main_list:
        status =True
    else:
        status = False
print(status)            





