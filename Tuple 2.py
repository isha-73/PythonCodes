# Isha Bule UCE2021610
# Tuple part 2

myTuple =("apple","Mana","Chery","Cherry",4556)
print(myTuple)
print(type(myTuple))

set1={"the set",7,"y"}
set2={"zerox","Yellow",2,"Air","Air"}
print(type(set1))
print(set1)
print(set2)
print(len(myTuple))
print(len(set2))


tup1=(23,67,"tuple")
tup2=("concatenation",)
tup3=tup1+tup2
print(tup3)
tup4=(tup1,tup2)
print(tup4)

list1=[1,2,4,"ho"]
list2=[78,52,"ji"]
list3=[list1,list2]
print(list3)


print(tup2*3)
lisst=list(tup1)
lisst.append("hello")
lisst.insert(2,"HI")
lisst.remove("hello")
tup1=tuple(lisst)
print(tup1)

'''
************ OUTPUT ************

('apple', 'Mana', 'Chery', 'Cherry', 4556)
<class 'tuple'>
<class 'set'>
{'the set', 'y', 7}
{'zerox', 2, 'Yellow', 'Air'}
5
4
(23, 67, 'tuple', 'concatenation')
((23, 67, 'tuple'), ('concatenation',))
[[1, 2, 4, 'ho'], [78, 52, 'ji']]
('concatenation', 'concatenation', 'concatenation')
(23, 67, 'HI', 'tuple')

Process finished with exit code 0

'''