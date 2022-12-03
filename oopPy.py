#Isha Bule UCE2021610
# OOP in PYTHON implementation

class Employee(object):
    def __init__(self, EmpNo, EmpName, Post, salary, Department):
        self.EmpNo = EmpNo
        self.EmpName = EmpName
        self.Post = Post
        self.salary = salary
        self.Department = Department

    def DisplayData(self):
        print(self.EmpNo, " ", self.EmpName, " ", self.Department, " ", self.Post, " ", self.salary)


k = 0
EmpList = []
for i in range(3):
    name = input("Enter the name of emplyee %i " % (i + 1))
    post = input("Enter the post of emplyee %i " % (i + 1))
    salary = input("Enter the salary of emplyee %i " % (i + 1))
    Department = input("Enter the department of empl0yee %i " % (i + 1))
    num = i + 1
    EmpList.append(Employee(num, name, post, salary, Department))
    k = i + 1

for i in range(3):
    # print(EmpList[i].EmpName)
    EmpList[i].DisplayData()


def AddEmployee():
    name = input("Enter the name of new emplyee")
    post = input("Enter the post of new emplyee")
    salary = input("Enter the salary of new employee")
    Department = input("Enter the department of employee")
    global k
    num = k + 1
    k = k + 1
    EmpList.append(Employee(num, name, post, salary, Department))
    for n in range(k):
        # print(EmpList[i].EmpName)
        EmpList[n].DisplayData()


def DeleteEmployee():
    num1 = int(input("Enter employee number, to delete it from list"))
    for j in range(k - 1):
        if (num1 == EmpList[j].EmpNo):
            del EmpList[j]
    for n in range(k - 1):
        # print(EmpList[i].EmpName)
        EmpList[n].DisplayData()


def updatedetails():
    num1 = int(input("Enter employee number, to update its data"))
    count = 0
    for j in range(k - 1):
        if num1 == EmpList[j].EmpNo:
            EmpList[j].EmpName = input("Enter the updated name of employee ")
            EmpList[j].Post = input("Enter the updated post ")
            EmpList[j].salary = input("Enter the updated salary ")
            EmpList[j].DisplayData()
            count += 1
    if count == 0:
        print("Eployee doesnt exist!!")


def searchEmployee():
    num1 = int(input("Enter employee number, to search"))
    count = 0
    for j in range(k - 1):
        if num1 == EmpList[j].EmpNo:
            EmpList[j].DisplayData()


choice = 0
while choice != 6:
    print("MENU:\n1-ADD NEW EMPLOYEE\n2-DELETE AN EMPLOYEE")
    print("4-UPDATE FIELDS OF EMPLOYEE\n5-SEARCH EMPLOYEE\n6-EXIT")
    choice = int(input("ENTER YOUR CHOICE: "))  # displaying menu and inputing choice
    if choice == 1:
        print("YOU HAVE CHOSEN: 1-ADD NEW EMPLOYEE")
        AddEmployee()

    elif choice == 2:
        print("YOU HAVE CHOSEN: 2-DELETE AN EMPLOYEE")
        DeleteEmployee()


    elif choice == 4:
        print("YOU HAVE CHOSEN: 4-UPDATE FIELDS OF EMPLOYEE")
        updatedetails()

    elif choice == 5:
        print("YOU HAVE CHOSEN: 5-SEARCH EMPLOYEE")
        searchEmployee()


    elif (choice == 6):
        print("YOU HAVE CHOSEN: 6-EXIT")
        break
    else:  # default case: wrong input of choice
        print("Wrong input of choice")


'''
E:\PyCharm\venv\Scripts\python.exe E:/PyCharm/oopPy.py
Enter the name of emplyee 1 Isha Bule
Enter the post of emplyee 1 SWE
Enter the salary of emplyee 1 8500000
Enter the department of empl0yee 1 CS
Enter the name of emplyee 2 Tilak Dave
Enter the post of emplyee 2 CEO
Enter the salary of emplyee 2 1200000000
Enter the department of empl0yee 2 CS
Enter the name of emplyee 3 Shravani B
Enter the post of emplyee 3 SWE
Enter the salary of emplyee 3 50000
Enter the department of empl0yee 3 CS
1   Isha Bule   CS   SWE   8500000
2   Tilak Dave   CS   CEO   1200000000
3   Shravani B   CS   SWE   50000
MENU:
1-ADD NEW EMPLOYEE
2-DELETE AN EMPLOYEE
4-UPDATE FIELDS OF EMPLOYEE
5-SEARCH EMPLOYEE
6-EXIT
ENTER YOUR CHOICE: 1
YOU HAVE CHOSEN: 1-ADD NEW EMPLOYEE
Enter the name of new emplyeeSarthak Bule
Enter the post of new emplyeeSWE
Enter the salary of new employee8500
Enter the department of employeeCS
1   Isha Bule   CS   SWE   8500000
2   Tilak Dave   CS   CEO   1200000000
3   Shravani B   CS   SWE   50000
4   Sarthak Bule   CS   SWE   8500
MENU:
1-ADD NEW EMPLOYEE
2-DELETE AN EMPLOYEE
4-UPDATE FIELDS OF EMPLOYEE
5-SEARCH EMPLOYEE
6-EXIT
ENTER YOUR CHOICE: 2
YOU HAVE CHOSEN: 2-DELETE AN EMPLOYEE
Enter employee number, to delete it from list3
1   Isha Bule   CS   SWE   8500000
2   Tilak Dave   CS   CEO   1200000000
4   Sarthak Bule   CS   SWE   8500
MENU:
1-ADD NEW EMPLOYEE
2-DELETE AN EMPLOYEE
4-UPDATE FIELDS OF EMPLOYEE
5-SEARCH EMPLOYEE
6-EXIT
ENTER YOUR CHOICE: 4
YOU HAVE CHOSEN: 4-UPDATE FIELDS OF EMPLOYEE
Enter employee number, to update its data2
Enter the updated name of employee D Tilak
Enter the updated post Founder
Enter the updated salary 520000000
2   D Tilak   CS   Founder   520000000
MENU:
1-ADD NEW EMPLOYEE
2-DELETE AN EMPLOYEE
4-UPDATE FIELDS OF EMPLOYEE
5-SEARCH EMPLOYEE
6-EXIT
ENTER YOUR CHOICE: 5
YOU HAVE CHOSEN: 5-SEARCH EMPLOYEE
Enter employee number, to search1
1   Isha Bule   CS   SWE   8500000
MENU:
1-ADD NEW EMPLOYEE
2-DELETE AN EMPLOYEE
4-UPDATE FIELDS OF EMPLOYEE
5-SEARCH EMPLOYEE
6-EXIT
ENTER YOUR CHOICE: 6
YOU HAVE CHOSEN: 6-EXIT

Process finished with exit code 0
'''