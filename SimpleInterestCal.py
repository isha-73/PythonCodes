
# Simple Interest Calculation
principle = float(input("Enter the principle amount "))
rate = float(input("Enter the rate of interest in % "))
num = int((input("Enter the period of investment ")))
# calculating simple interest
product = float(principle*rate*num)
interest = float(product / 100)
print("The simple interest is", interest)


#****************** Output ***************************
'''
Enter the principle amount 50000
Enter the rate of interest 2
Enter the period of investment 3
The simple interest is 3000.0

Process finished with exit code 0
'''
