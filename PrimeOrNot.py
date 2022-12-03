
# check whether number is prime or not
number = int(input("Enter any number "))
if number > 1:
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            print(number, "number is not prime")
            break
        else:
            print(number, "number is prime")
else:
    print(number, "is a prime number")

# ************** OUTPUT ************
''' Enter any number  6
6 number is not prime

Process finished with exit code 0

'''
