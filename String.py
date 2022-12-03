
# Isha Bule UCE2021610
# Implementing string and its functions
#Part1:
list1 = ["I", "am", "the", "Student", "of", "Cummins", "College"]
string = ""
for i in range(len(list1)):
    string = string + " " + (list1[i])
print(string)


def countfun(string):
    string = string.split()  # oir I could use len(list)
    for i in string:
        print("(", len(i), ") words in ", i)


countfun(string)

print(string.isupper())


def Map(string):
    open = list(map(len, string.split()))
    print(open)


Map(string)

#Part2:

'''  Part1: Strings in python:
    1: Lenght of strings
    2:Reverse the string
    3:Concatenation of two strings
    4:Comparison of two strings
    \5:Substring
    6: Position of characters
    7:St6ring imn lowercase
    8:Upper case
    9:replace character in string
    10.ignoring the cases
    11.ccheckl whetther it is palindrome or not

    '''
print(
    " 1: Lenght of strings\n2:Reverse the string\n3:Concatenation of two strings\n4:Comparison of two strings\n5:Substring\n6: Position of characters\n7:St6ring imn lowercase\n8:Upper case\n9:replace character in string\n10.ignoring the cases \n 11.ccheckl whetther it is palindrome or not")
str1 = "Hello I am learning Python as well as DSA"
i = len(str1)
str2 = str1[::-1]
print('Length of the string = "Hello I am learning Python as well as DSA" is ', i)
print()
print("Reverse string : ", str2)
print()

A = " Hello "
B = "Cummins "
C = "College"
S = A + B + C
print("Printing conxcatenatiuon of strings A,B,c : ", S)
print()

String1 = "COMPARISON"
String2 = "comparison"
String3 = "comparison"
print('is "COMPARISON" & "comparison" same? ', String1 == String2)
print('is "comparison" & "comparison" same? ', String3 == String2)

print()

substring = S[0:6]
print("Substring of string S is ", substring)

print()
print("o in string at ", C.index("o"))
print("l in string at : ")
for i in range(len(C)):
    if "l" == C[i]:
        print(i)

print()
print(str1.lower())
print()
print(str1.upper())

print()
print(A.replace(" ", "*"))
print()


def isPalindrome():
    lang = "MALAYALAM"
    if lang == lang[::-1]:
        print("Malayalam is palindrome")
    else:
        print("It is not palindrome")


isPalindrome()


def ignoreCase():
    strrrr1 = input("Enter any string")
    strrrr2 = input("Enter again any string")

    print("Ignoring Cases , whether both strings are equal?? ", strrrr1.upper() == strrrr2.upper())


ignoreCase()


# ********** OUTPUT ************
'''
 I am the Student of Cummins College
( 1 ) words in  I
( 2 ) words in  am
( 3 ) words in  the
( 7 ) words in  Student
( 2 ) words in  of
( 7 ) words in  Cummins
( 7 ) words in  College
False
[1, 2, 3, 7, 2, 7, 7]
 1: Lenght of strings
2:Reverse the string
3:Concatenation of two strings
4:Comparison of two strings
5:Substring
6: Position of characters
7:St6ring imn lowercase
8:Upper case
9:replace character in string
10.ignoring the cases 
 11.ccheckl whetther it is palindrome or not
Length of the string = "Hello I am learning Python as well as DSA" is  41

Reverse string :  ASD sa llew sa nohtyP gninrael ma I olleH

Printing conxcatenatiuon of strings A,B,c :   Hello Cummins College

is "COMPARISON" & "comparison" same?  False
is "comparison" & "comparison" same?  True

Substring of string S is   Hello

o in string at  1
l in string at : 
2
3

hello i am learning python as well as dsa

HELLO I AM LEARNING PYTHON AS WELL AS DSA

*Hello*

Malayalam is palindrome
Enter any string Hello
Enter again any string Bye
Ignoring Cases , whether both strings are equal??  False

Process finished with exit code 0'''

