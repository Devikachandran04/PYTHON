#prime
n=int(input("enter the number"))
flag=0
for i in range(2,int(n/2)):
    if n%i==0:
        flag=1
        break
if flag==0:
        print("its prime")
else:
        print("not prime")
    


