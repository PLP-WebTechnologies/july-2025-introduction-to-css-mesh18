for i in range(1,4):
    for j in range(1,4):
        print(i,j)

#creating a 2 by 3 matrix
print("creating a matrix")
matrix = []
for i in range(2):
    rows = []
    for j in range(3):
        rows.append(j)
    matrix.append(rows)

print(matrix)
print(rows)