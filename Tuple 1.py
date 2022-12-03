# Isha Bule UCE2021610
# Tuple part 1

#sort tuple

#tuple1=(2,'j',456,'io',78,'a',10)
tuple1=(7,8,9,4,5,6,1,2,3)
set1=set(tuple1)
tuple1=set1
print(tuple1)
print("***************************************************")

list1=[("sort",'i'),('t','k:','467','10','45'),("Isha","7845"),("1","7","2")]
list1.sort()
print(list1)

print("***************************************************")
for i in range(len(list1)):
    print(list1[i])

print("***************************************************")

for i in range(len(list1)):
    temp= list(list1[i])
    temp.sort()
    list1[i]=tuple(temp)

print(list1)

#********** OUTPUT **********
'''
E:\PyCharm\venv\Scripts\python.exe "E:/PyCharm/Tuple 1.py"
{1, 2, 3, 4, 5, 6, 7, 8, 9}
***************************************************
[('1', '7', '2'), ('Isha', '7845'), ('sort', 'i'), ('t', 'k:', '467', '10', '45')]
***************************************************
('1', '7', '2')
('Isha', '7845')
('sort', 'i')
('t', 'k:', '467', '10', '45')
***************************************************
[('1', '2', '7'), ('7845', 'Isha'), ('i', 'sort'), ('10', '45', '467', 'k:', 't')]

Process finished with exit code 0
'''