n=int(input("Enter number of rows "))
m=int(input("Enter number of columns "))
mat=[]
print("Enter elements :")
for i in range(0,n):
    arr=[]
    for j in range(0,m):
        z=int(input())
        arr.append(z)
    mat.append(arr)

print("Original Matrix: ")
for i in range(0,n):
    for j in range(0,m):     
        print(mat[i][j],end=" ")
    print()

for i in range(0,n):
        for j in range(i,m):
                temp=mat[i][j]
                mat[i][j]=mat[j][i]
                mat[j][i]=temp

print("Matrix after transpose")
for i in range(0,n):
    for j in range(0,m):     
        print(mat[i][j],end=" ")
    print()

for j in range(0,m):
        c=1
        i=0
        while c<=m-1:
                c=c+1
                temp=mat[i][j]
                mat[i][j]=mat[n-1-i][j]
                mat[n-1-i][j]=temp
                i=i+1

print("Matrix after rotation by 90 degree anti-clockwise")
for i in range(0,n):
    for j in range(0,m):     
        print(mat[i][j],end=" ")
    print()

