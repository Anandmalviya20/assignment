#Write a Python program to create a dictionary from a string. 
#Track the count of the letters from the string. 
name = input("enter name: ")
count_dic={}
for letter in name :
    if letter in count_dic:
        count_dic[letter]+=1
    else :
        count_dic[letter]=1
print(count_dic) 
#USING FUNCTION 
def letter_count(name):
    count_dic={}
    for letter in name :
        if letter in count_dic:
            count_dic[letter]+=1
        else:
            count_dic[letter]=1
    print(count_dic)
name = input("enter name: ")    
letter_count(name)              








