x=input("enter the string") 
u=0 
l=0 
d=0

for i in x:

    if(i.isupper()): 
        u=u+1 
    elif(i.islower()): 
        l=l+1 
    elif(i.isdigit()): 
        d=d+1 
print("uppercase", u) 
print("lowercase", l) 
print("digit", d)