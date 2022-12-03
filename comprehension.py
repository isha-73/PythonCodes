list1 = []
for i in range(10):
    j = i ** 2
    list1.append(j)
print(list1)
# ...we can use a list comprehension
list2 = [x ** 2 for x in range(10)]
print(list2)

list3 = [x ** 2 for x in range(10) if x > 5]  # with a conditional statament
print(list3)

set1 = {x ** 2 for x in range(10)}  # set comprehension
print(set1)


dict1 = {x: x ** 2 for x in range(10)}  # dictionary comprehension
print(dict1)