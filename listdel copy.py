# Example list to be sorted
array = [1.1,14,54,33,8,1]

# Length of the array
n = len(array)

# Bubble Sort Algorithm
for i in range(n):
    # Track if a swap is made
    for j in range(0, n-i-1):
        # Compare two adjacent elements
        if array[j] > array[j+1]:
            # Swapping elements if they are not in the intended order
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
    # If no two elements were swapped in the inner loop, the array is sorted
   

print('Sorted Array in Ascending Order:')
print(array)
