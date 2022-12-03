# Isha Bule UCE2021610
# factorial of number
num = 7
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

# ******* OUTPUT *******
'''
The factorial of 7 is 5040

Process finished with exit code 0
'''