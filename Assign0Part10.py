
# Pattern
j = 0
rows = int(input("Enter the number of rows-"))
i = rows
while i > 0:
    j = i
    while j > 0:
        print("*", end=" ")
        j -= 1
    print()  # shape is discrete
    i -= 1

'''
Enter the number of rows-5
* * * * * 
* * * * 
* * * 
* * 
* 

Process finished with exit code 0
'''
