matr2 = [
        [2,6,12],
        [2,15,3],
        [1,8,3]
]
rows = len(matr2)
cols = len(matr2[0])
matr1 = []
for i in range(1,rows-1):
    row = []
    for j in range(1,cols-1):
        row.append(matr2[i][j])
    matr1.append(row)
for row in matr1:
    print(row)


