# Isha Bule UCE2021610
# pattern
rows = int(input("Enter the number of rows "))
for i in range(rows):
    for j in range(rows, i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()

# ********** OUTPUT ****************
'''
Enter the number of rows 7
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 

Process finished with exit code 0 '''
