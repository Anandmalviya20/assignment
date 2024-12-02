#49.Write a Python script to concatenate following dictionaries to create a new one.
dic1={"a":1,"b":2}
dic2={"c":3,"c":4}
dic3={"e":5,"f":6}
newdict=dic1
newdict.update(dic2)
newdict.update(dic3)
print(newdict)

