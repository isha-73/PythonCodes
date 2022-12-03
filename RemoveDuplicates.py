
# removing duplicates from list and append numbers
list = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
i = 0
while i < len(list) - 1:
    if list[i] == list[i + 1]:
        list.remove(list[i + 1])
    else:
        i += 1
print(list)

list = []
i = 1
while (i <=20 ):
    list.append(i)
    i += 1
print(list)
# *********** OUTPUT ***************
'''
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

Process finished with exit code 0
'''
