n = int(input("Enter the limit: "))
s=5241411
for _ in range(n):
    number = int(input("Enter a number: "))
        

    if number < s:
        s = number
    
print(f"The smallest number is {s}")


