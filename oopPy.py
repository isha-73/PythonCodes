
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

