# Map and Filter

# map() - takes a function and a sequence as arguments and applies the function to all the elements of the sequence,
# returning a list as the result
def product10(a,b):
    return a * b


list1 = range(10)
list2 = range(5)
res = map(product10, list2, list1)
# result is [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]; applying the product10() function to
# each element of list1
print("First map of mult iterable", list(res))
# or...

res2 = map((lambda a: a * 10), list1)  # result is [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] as well
print(list(res2))
# filter() - takes a function and a sequence as arguments and extracts all the elements in the list for which the
# function returns True
filt = filter(lambda a: a > 5, list1)  # result is [6, 7, 8, 9]
print(list(filt))
