# Isha Bule UCE2021610
# Addition of even numbers in series

total = 0
end = int(input("Enter the end of the series:"))
for num in range(1, end + 1):
    if num % 2 == 0:
        total = total + num
print(total)

# ************* OUTPUT ***************
'''
Enter the end of the series:5
6

Process finished with exit code 0'''
