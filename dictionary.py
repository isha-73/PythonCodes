# Isha Bule UCE2021610
# Use of dictionary

myDict = {"Chase": "Pursuit", "Legacy": "Heritage", "Bizarre": "Uncanny"}


def addWord(key, value):
    myDict[key] = value


def sortDict():
    for i in sorted(myDict):
        print((i, myDict[i]), end=" ")


def search(key):
    print(key, ":", myDict[key])


def remove(key):
    del myDict[key]


def sameMeaning():
    for i in sorted(myDict):
        temp = myDict[i]
        print(i, end=":")
        for j in sorted(myDict):
            if (temp == myDict[j]):
                print(myDict[j])


addWord("house", "home")
remove("Legacy")
search("Chase")
sameMeaning()
sortDict();

# ***********OUTPUT**********
'''
Chase : Pursuit
Bizarre:Uncanny
Chase:Pursuit
house:home
('Bizarre', 'Uncanny') ('Chase', 'Pursuit') ('house', 'home') 
Process finished with exit code 0
'''
