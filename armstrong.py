#armstrong of a number
n=int(input("enter the number"))
a=r=0
m=n
while n>0:
    a=n%10
    r=r+a*a*a
    n=int(n/10)
if m==r:
     print("yes")
else:
    print("no")

'''n = int(input("Enter the number: "))
a = r = 0
m = n

while n > 0:
    a = n % 10
    r = r + a **3
    n = n // 10

if m == r:
    print("Yes, it's an Armstrong number.")
else:
    print("No, it's not an Armstrong number.")'''

