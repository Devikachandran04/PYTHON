'''a=input("enter a\n")
b=input("enter b\n")

temp=a
a=b
b=temp
#a and b are strings in "" just to show that which has swapped or if we can change the variable declaration at first
print("a=" +a +"\n" +"b=" + b)'''

def h(x):
    (d,n) = (1,0)
    while d <= x:
        (d,n) = (d*3,n+1)
    return(n)
