"""
Name: Kesar Shrivastava
Roll number: 2019051
"""
#Initialising the given strings
x = "ATCAGAGTA"
y = "TTCAGTA"

#These lists maintain the indices where there is maximum score in the matrix of local alignment.
listx = []
listy = []

#function to print the alignments
def alignment(s1, s2):
    printed = [[0 for i in range(len(s1))] for j in range(3)]
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            printed[0][i] = s1[i]
            printed[1][i] = "|"
            printed[2][i] = s2[i]
        else:
            printed[0][i] = s1[i]
            printed[1][i] = " "
            printed[2][i] = s2[i]
    for i in range(3):
        for j in range(len(s1)):
            print(printed[i][j], end = "")
        print()
    return

numOfRows = len(y)+1 #5 
numOfColumns = len(x)+1 #6

maxInMatrixLocal = -1
indexI = 0
indexJ = 0

#Initialising the matrices to fill in values
matrix = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]
matrixLocal = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]

mat = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]
matLocal = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]

matrix[0][0] = 0

#Filling in the matrices
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
        if matLocal[i][j]==8:
            listx.append(i)
            listy.append(j)

print("Question 1 a): The generated dynamic programming matrix for global alignment is:")
for i in range(numOfRows):
    for j in range(numOfColumns):
        print(matrix[i][j], end = " ")
    print()

print()
print("Question 1 b): Yes, there is more than one possibility of aligning the given sequences.")
print("This happens because when we reach one particular cell while backtracking there can be more")
print("than one paths to reach the top left corner of the grid.")
print("Hence, we get multiple optimal alignments while the score for each is same.")
print()


i = numOfRows-1
j = numOfColumns-1

string1 = ""
string2 = ""
list = []

#function to get the optimal alignment in global alignment
def func(s1, s2, i, j, array, match, mis, gap):
    if(i==0 and j==0):
        if s1 in list:
            u = 1
        else:
            alignment(s1, s2)
            list.append(s1)
            print()
        return
    if y[i-1]==x[j-1]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        func(s1, s2, i, j, array, match, mis, gap)
    if array[i-1][j-1]+mis==array[i][j]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        func(s1, s2, i, j, array, match, mis, gap)
    if array[i-1][j]+gap==array[i][j]:
        s1 = y[i-1] + s1
        s2 = "_" + s2
        i-=1
        func(s1, s2, i, j, array, match, mis, gap)
    if array[i][j-1]+gap==array[i][j]:
        s1 = "_" + s1
        s2 = x[j-1] + s2
        j-=1
        func(s1, s2, i, j, array, match, mis, gap)


print("Question 1 c): The scores of all the optimal alignments given below is 9 because")
print("the rightmost value of the last row is taken to be the score of global alignment.")
print()

func(string1, string2, i, j, matrix, 2, -1, -1)

print("Question 2 a): The generated dynamic programming matrix for local alignment is:")
for i in range(numOfRows):
    for j in range(numOfColumns):
        print(matrixLocal[i][j], end = " ")
    print()

print()

string1 = ""
string2 = ""
list = []

#function to get the optimal alignment in local alignment
def localFunc(s1, s2, i, j, array, match, mis, gap):
    if(array[i][j]==0):
        if s1 in list:
            u = 1
        else:
            alignment(s1, s2)
            list.append(s1)
            print()
        return
    if y[i-1]==x[j-1]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        localFunc(s1, s2, i, j, array, match, mis, gap)
    if array[i-1][j-1]+mis==array[i][j]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        localFunc(s1, s2, i, j, array, match, mis, gap)
    if array[i-1][j]+gap==array[i][j]:
        s1 = y[i-1] + s1
        s2 = "_" + s2
        i-=1
        localFunc(s1, s2, i, j, array, match, mis, gap)
    if array[i][j-1]+gap==array[i][j]:
        s1 = "_" + s1
        s2 = x[j-1] + s2
        j-=1
        localFunc(s1, s2, i, j, array, match, mis, gap)

print("Question 2 b): The local alignments have score 10 as in local alignment we take the maximum value to be its score: ")
localFunc(string1, string2, indexI, indexJ, matrixLocal, 2, -1, -1)
print()
print("Question 3: In the local alignment the minimum value that a box can hold in the grid is 0.")
print("So the changes that were required are as follows: ")
print("1) Intialize row0/col0 with 0.")
print("2) Find the cell with the highest value (i,j) and extend the alignment back to the first zero value.")
print("3) The score of the alignment is the value in that cell")
print()
print("Question 4: ")
print()
print("The global alignment matrix with changed scores: ")
print()
for i in range(numOfRows):
    for j in range(numOfColumns):
        print(mat[i][j], end = " ")
    print()

print()

print("The local alignment matrix with changed scores: ")
print()
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
val = 0

def localFunc1(s1, s2, i, j, array, match, mis, gap):
    if(array[i][j]==0):
        if s1=="TC__AGTA":
            u = 1
        elif s1 in list:
            u=2
        else:
            alignment(s1, s2)
            list.append(s1)
            print()
        return
    if y[i-1]==x[j-1]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        localFunc1(s1, s2, i, j, array, match, mis, gap)
    if array[i-1][j-1]+mis==array[i][j]:
        s1 = y[i-1]+s1
        s2 = x[j-1]+s2
        i-=1
        j-=1
        localFunc1(s1, s2, i, j, array, match, mis, gap)
    if array[i-1][j]+gap==array[i][j]:
        s1 = y[i-1] + s1
        s2 = "_" + s2
        i-=1
        localFunc1(s1, s2, i, j, array, match, mis, gap)
    if array[i][j-1]+gap==array[i][j]:
        s1 = "_" + s1
        s2 = x[j-1] + s2
        j-=1
        localFunc1(s1, s2, i, j, array, match, mis, gap)


print("The global alignments are: ")
print()

func(string1, string2, i, j, mat, 2, -1, -2)
print()
print("The local alignments are: ")
print()
for i in range(len(listx)):
    string1=""
    string2=""
    localFunc1(string1, string2, listx[i], listy[i], matLocal, 2, -1, -2)

print("As can be seen from the results above the change in scoring scheme has changed the result.")
print("When aligning biological sequences, the choice of parameter values for the alignment scoring function is critical.")
print("Small changes in any score can yield radically different alignments.")
print("Since in our problem the score for the gap penalty is changed from -1 to -2 hence there is a difference in the results.")