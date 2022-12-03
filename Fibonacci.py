
# Fibonacci series

terms = int(input("Enter number of terms:"))
n1, n2 = 0, 1
count = 0

if terms <= 0:
    print("Please enter a positive integer")
elif terms == 1:
    print("Fibonacci sequence upto", terms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(n1, end="->")
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
print("End")

'''
Enter number of terms:10
Fibonacci sequence:
0->1->1->2->3->5->8->13->21->34->End

Process finished with exit code 0'''
