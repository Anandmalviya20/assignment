#48.Write a Python script to sort (ascending and descending) a dictionary by value. 
a = {"a":3,"b":1,"c":4,"d":2}
# ascending
sor = dict(sorted(a.items(),key= lambda items :items[1]))
print(sor)
# descending 
sor = dict(sorted(a.items(),key=lambda items : items[1],reverse = True))
print(sor)




