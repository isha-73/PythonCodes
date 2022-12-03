# Isha Bule UCE2021610
# File handling

newFile = open("File_Handling.py", 'w')
newFile.write("This is the python program on file handling...")
newFile = open("File_Handling.py", 'r')
print(newFile.readline())
newFile = open("File_Handling.py", 'w')
newFile.writelines("Hello "
                   "hello "
                   "this is multiline code")
newFile = open("File_Handling.py", 'r')
print(newFile.readline())
newFile.close()

new = open("File_Handling.py", 'r')
for x in new:
    print(x)  # reading all the lines one by one

new.seek(10)  # seek data after position 10
print(new.readline())
print("position of cursor", new.tell())  # tell function returns position of cursor
'''
*******OUTPUT**********
This is the python program on file handling...
Hello hello this is multline code
Hello hello this is multline code
o this is multline code
position before readline  33
'''