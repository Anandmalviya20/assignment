#56) Write a Python program to map two lists into a dictionary 
'''Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, '': 300}). '''
from collections import Counter
keys =['a','b','c','d']
values =[400,400,400,300]
dic = dict(zip(keys,values))
cou_dic = Counter(dic)
print(cou_dic)







