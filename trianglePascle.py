
# Pascal Triangle using List in Python

n = int(input("Enter the number of rows in pascal triangle "))
list = []
for i in range(n):
    list2 = []
    for j in range(i + 1):
        if j == 0 or j == i:
            list2.append(1)
        else:
            list2.append(list[i - 1][j - 1] + list[i - 1][j])
    list.append(list2)
print(list)
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(list[i][j], end=" ")
    print()
 # ************** OUTPUT *****************
'''
Enter the number of rows in pascal triangle 6
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
1 5 10 10 5 1 

Process finished with exit code 0 '''
