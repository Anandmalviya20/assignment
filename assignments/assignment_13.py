#program that will return true if the two given integer values are equal or their sum or difference is 5. 
a= int(input("enter 1st value: "))
b= int(input("enter 2nd value: "))
if a ==b or (b-a)==5 or (b+a)==5:
    print("This is true ")
else :
    print("false")    
