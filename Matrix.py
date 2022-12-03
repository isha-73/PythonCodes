# Isha Bule

rows = int(input("Enter the number of rows in matrix 1 "))
column = int(input("Enter the number of columns "))
matrix1 = []
print("Enter the elemts of matrix1 row-wise")
for i in range(rows):
    temp = []

    for j in range(column):
        temp.append(int(input()))
    matrix1.append(temp)

print("Matrix 1 is ")
for i in range(rows):
    for j in range(column):
        print(matrix1[i][j], end=" ")
    print()
rows2 = int(input("Enter the number of rows in matrix 2 "))
column2 = int(input("Enter the number of columns "))
matrix2 = []
print("Enter the elemts of matrix2 row-wise")
for i in range(rows2):
    temp = []
    for j in range(column2):
        temp.append(int(input()))
    matrix2.append(temp)

print("Matrix 2 is ")
for i in range(rows2):
    for j in range(column2):
        print(matrix2[i][j], end=" ")
    print()


if rows == rows2 and column == column2:
    print("Addition of two matrices is")

    def addition():
        result = [[0 for k in range(column)] for l in range(rows)]
        for it in range(rows):
            for ct in range(column):
                result[it][ct] = matrix1[it][ct] + matrix2[it][ct]
                print(result[it][ct], end=" ")
            print()


    addition()

if column == rows2:
    def multiplication():
        print("Multiplication of two matrices ")
        res = [[0 for m in range(column2)] for n in range(rows)]
        for i in range(len(matrix1)):

            # iterating by column by B
            for j in range(len(matrix2[0])):

                # iterating by rows of B
                for k in range(len(matrix2)):
                    res[i][j] += matrix1[i][k] * matrix2[k][j]

        for r in range(rows):
            for c in range(column2):
                print(res[r][c], end=" ")
            print()


    multiplication()

    # *************** OUTPUT ********************
'''
Enter the number of rows in matrix 1 3
Enter the number of columns 3
Enter the elemts of matrix1 row-wise
5
5
3
2
5
5
5
5
5
Matrix 1 is 
5 5 3 
2 5 5 
5 5 5 
Enter the number of rows in matrix 2 3
Enter the number of columns 3
Enter the elemts of matrix2 row-wise
5
6
3
9
8
6
2
5
5
Matrix 2 is 
5 6 3 
9 8 6 
2 5 5 
Addition of two matrices is
10 11 6 
11 13 11 
7 10 10 
Multiplication of two matrices 
76 85 60 
65 77 61 
80 95 70 

Process finished with exit code 0'''