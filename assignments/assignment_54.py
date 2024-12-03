#Write a Python program to check multiple keys exists in a dictionary 
def key_exists(dictionary,key):
    if key in dictionary:
        return True
    else:
        return False    
dic = {"a":3,"b":1,"c":4,"d":2}
key_to_check ="e"
if key_exists(dic,key_to_check):
    print(f"{key_to_check} exists in the dictionary.")
else:
    print(f"{key_to_check} does not exist in the dictionary.")