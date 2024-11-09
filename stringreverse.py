'''s=input("enter a string ")
rev=" "
j=len(s)
for i in range (len(s)):
    rev=rev+s[j-1]
    j=j-1
print(rev)'''


s="phuwin"
t="ppnaravit"
c=cmp(s,t)
if c==0:
    print("yes")
else:
    print(c,"no")




