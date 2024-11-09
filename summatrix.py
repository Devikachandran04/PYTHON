# Input the dimensions of the matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize empty matrices
matrix1 = []
matrix2 = []
result_matrix = []

# Input elements for the first matrix
print("Enter the elements for matrix 1:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Element  "))
        row.append(element)
    matrix1.append(row)

# Input elements for the second matrix
print("Enter the elements for matrix 2:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Element"))
        row.append(element)
    matrix2.append(row)

# Calculate the sum of the two matrices
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(row)

# Print the result matrix
print("Result Matrix:")
for row in result_matrix:
    print(row)
