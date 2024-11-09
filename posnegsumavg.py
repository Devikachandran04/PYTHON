x=int(input("enter a kii"))
ps=pav=ns=nav=0
p=n=0
while x!=0:
    s=int(input("enter a number"))
    if s>0:
        ps=ps+s
        p=p+1
    
    else:
        ns=ns+s
        n=n+1
    x=x-1
print(ps)
print(ns)
print(p)
print(n)
pav=ps/p
nav=ns/n
print(pav)
print(nav)

'''n = int(input("Enter the count: "))
pos = 0
neg = 0
c1 = 0
c2 = 0
avg1 =0
avg2 =0
for i in range(n):
    x = int(input("Enter a number: "))
    if x > 0:
        pos =pos+x
        c1 =c1+1
    elif x < 0:
        neg =neg+x
        c2 =c2+1


avg1 = pos / c1
avg2 = neg / c2

print("The sum of positive numbers is:", pos)
print("The sum of negative numbers is:", neg)
print("The average of positive numbers is:", avg1)
print("The average of negative numbers is:", avg2)'''