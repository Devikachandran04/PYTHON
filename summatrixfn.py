mat3=[]
m=int(input("enter the no of rows of matrix"))
n=int(input("enter the no of colof matrix "))

def read_matrix():
  mat=[]
  
  for i in range(m):
     row=[]
     for j in range(n):
         x=int(input("enter the element"))
         row.append(x)
     mat.append(row)
  return (mat)

def print_matrix(mat):
 
 for i in range(m):
   for j in range(n):
    print(mat[i][j],end=" ")
   print("")

def sum_matrix(m1,m2):
  for i in range(m):
    row=[]
    for j in range(n):
      x=m1[i][j]+m2[i][j]
      row.append(x)
    mat3.append(row) 
  print_matrix(mat3)

#READING NO.OF ROWS&COLUMNS


mat1=read_matrix()
print("matrix1")
print_matrix(mat1)
mat2=read_matrix()
print("matrix2")
print_matrix(mat2)

print("sum of matices")
sum_matrix(mat1,mat2)