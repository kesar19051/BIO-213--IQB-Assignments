x = "ATCAGAGTA"
y = "TTCAGTA"

numOfRows = len(y)+1 #5 
numOfColumns = len(x)+1 #6

matrix = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]

matrix[0][0] = 0

for i in range(1, numOfColumns):
    matrix[0][i] = matrix[0][i-1]-1

for i in range(1, numOfRows):
    matrix[i][0] = matrix[i-1][0]-1

for i in range(1, numOfRows):
    for j in range(1, numOfColumns):
        if y[i-1]==x[j-1]:
            matrix[i][j] = max(max(matrix[i-1][j]-1, matrix[i][j-1]-1), matrix[i-1][j-1]+2)
        else:
            matrix[i][j] = max(max(matrix[i-1][j]-1, matrix[i][j-1]-1), matrix[i-1][j-1]-1)

for i in range(numOfRows):
    for j in range(numOfColumns):
        print(matrix[i][j], end = " ")
    print()

xpos = numOfRows+numOfColumns-2
ypos = numOfRows+numOfColumns-2

i = numOfRows-1
j = numOfColumns-1

s1 = ["" for x in range(numOfRows+numOfColumns+1)]
s2 = ["" for x in range(numOfRows+numOfColumns+1)]

while(i!=0 or j!=0):
    if y[i-1]==x[j-1]:
        s1[xpos] = y[i-1]
        s2[ypos] = x[j-1]
        i-=1
        j-=1
    elif matrix[i-1][j-1]-1==matrix[i][j]:
        s1[xpos] = y[i-1]
        s2[ypos] = x[j-1]
        i-=1
        j-=1
    elif matrix[i-1][j]-1==matrix[i][j]:
        s1[xpos] = y[i-1]
        s2[ypos] = "_"
        i-=1
    elif matrix[i][j-1]-1==matrix[i][j]:
        s1[xpos] = "_"
        s2[ypos] = x[j-1]
        j-=1
    xpos-=1
    ypos-=1
print(s1)
print(s2)