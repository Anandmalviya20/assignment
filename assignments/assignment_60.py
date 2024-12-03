name = 'w3resource'
count_dic={}
for letter in name :
    if letter in count_dic:
        count_dic[letter]+=1
    else :
        count_dic[letter]=1
print(count_dic) 