n = int(input("Enter the limit: "))
largest=second_largest=0
for _ in range(n):
    number = int(input("Enter a number: "))
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number


print(f"The largest number is {largest}")
print(f"The second largest number is {second_largest}")


