def max_value(matrix):
    max_val=float('-inf')

    for row in matrix:
        row_max=max(row)
        if max_val<row_max:
            max_val=row_max
    return max_val

print("Enter the Matrix")
mat=[]
for i in range(3):
    row=[]
    for j in range (3):
       val=int(input())
       row.append(val)
    mat.append(row)
maxval=0
maxval= max_value(mat)
print('The Max value is',maxval)