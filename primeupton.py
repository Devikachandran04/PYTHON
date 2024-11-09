# Input the limit
'''l = int(input("Enter the lower limit: "))
u = int(input("Enter the upper limit: "))
for num in range(l, u + 1):
    # Check if the number is prime
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            break
    else:
        print(num)'''




l = int(input("Enter the lower limit: "))
u = int(input("Enter the upper limit: "))
for i in range(l, u + 1):
    n=i
    x=n/2
    div=2
    flag=0
    while div<=x:
        if n%div==0:
            flag=1
            break
        div=div+1
    if flag==0:
         print(n)

