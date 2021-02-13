x = "ATCAGAGTA"
y = "TTCAGTA"

numOfRows = len(y)+1 #5 
numOfColumns = len(x)+1 #6

maxInMatrixLocal = -1
indexI = 0
indexJ = 0

matrix = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]
matrixLocal = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]

mat = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]
matLocal = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]

matrix[0][0] = 0

for i in range(1, numOfColumns):
    matrix[0][i] = matrix[0][i-1]-1
    mat[0][i] = mat[0][i-1]-2

for i in range(1, numOfRows):
    matrix[i][0] = matrix[i-1][0]-1
    mat[i][0] = mat[i-1][0]-2

for i in range(1, numOfRows):
    for j in range(1, numOfColumns):
        if y[i-1]==x[j-1]:
            matrix[i][j] = max(max(matrix[i-1][j]-1, matrix[i][j-1]-1), matrix[i-1][j-1]+2)
            matrixLocal[i][j] = max(max(max(matrixLocal[i-1][j]-1, matrixLocal[i][j-1]-1), matrixLocal[i-1][j-1]+2), 0)
        else:
            matrix[i][j] = max(max(matrix[i-1][j]-1, matrix[i][j-1]-1), matrix[i-1][j-1]-1)
            matrixLocal[i][j] = max(max(max(matrixLocal[i-1][j]-1, matrixLocal[i][j-1]-1), matrixLocal[i-1][j-1]-1), 0)
        if maxInMatrixLocal<=matrixLocal[i][j]:
            maxInMatrixLocal = matrixLocal[i][j]
            indexI = i
            indexJ = j

for i in range(1, numOfRows):
    for j in range(1, numOfColumns):
        if y[i-1]==x[j-1]:
            mat[i][j] = max(max(mat[i-1][j]-2, mat[i][j-1]-2), mat[i-1][j-1]+2)
            matLocal[i][j] = max(max(max(matLocal[i-1][j]-2, matLocal[i][j-1]-2), matLocal[i-1][j-1]+2), 0)
        else:
            mat[i][j] = max(max(mat[i-1][j]-2, mat[i][j-1]-2), mat[i-1][j-1]-1)
            matLocal[i][j] = max(max(max(matLocal[i-1][j]-2, matLocal[i][j-1]-2), matLocal[i-1][j-1]-1), 0)

print("The global alignment matrix: ")
for i in range(numOfRows):
    for j in range(numOfColumns):
        print(matrix[i][j], end = " ")
    print()

print()

print("The local alignment matrix: ")
for i in range(numOfRows):
    for j in range(numOfColumns):
        print(matrixLocal[i][j], end = " ")
    print()

print()

print("The global alignment matrix with changed scores: ")
for i in range(numOfRows):
    for j in range(numOfColumns):
        print(mat[i][j], end = " ")
    print()

print()

print("The local alignment matrix with changed scores: ")
for i in range(numOfRows):
    for j in range(numOfColumns):
        print(matLocal[i][j], end = " ")
    print()

print()

i = numOfRows-1
j = numOfColumns-1

string1 = ""
string2 = ""
list = []

def func(s1, s2, i, j, array):
    if(i==0 and j==0):
        if s1 in list:
            u = 1
        else:
            print(s1)
            print(s2)
            list.append(s1)
            print()
        return
    if y[i-1]==x[j-1]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        func(s1, s2, i, j, array)
    if matrix[i-1][j-1]-1==matrix[i][j]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        func(s1, s2, i, j, array)
    if matrix[i-1][j]-1==matrix[i][j]:
        s1 = y[i-1] + s1
        s2 = "_" + s2
        i-=1
        func(s1, s2, i, j, array)
    if matrix[i][j-1]-1==matrix[i][j]:
        s1 = "_" + s1
        s2 = x[j-1] + s2
        j-=1
        func(s1, s2, i, j, array)

func(string1, string2, i, j, matrix)

string1 = ""
string2 = ""
list = []

print("----------LOCAL-----------")

def localFunc(s1, s2, i, j, array):
    if(array[i][j]==0):
        if s1 in list:
            u = 1
        else:
            print(s1)
            print(s2)
            list.append(s1)
            print()
        return
    if y[i-1]==x[j-1]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        localFunc(s1, s2, i, j, array)
    if matrix[i-1][j-1]-1==matrix[i][j]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        localFunc(s1, s2, i, j, array)
    if matrix[i-1][j]-1==matrix[i][j]:
        s1 = y[i-1] + s1
        s2 = "_" + s2
        i-=1
        localFunc(s1, s2, i, j, array)
    if matrix[i][j-1]-1==matrix[i][j]:
        s1 = "_" + s1
        s2 = x[j-1] + s2
        j-=1
        localFunc(s1, s2, i, j, array)

localFunc(string1, string2, indexI, indexJ, matLocal)

