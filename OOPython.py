class Python(object):
    __j = 'Hell0'
    def __init__(self, data):
        self.data = data
        self.i = 0

    def function(self):
        print("This is data inside Python class : {},{}".format(self.data, self.i))
        print(self.__j)


obj = Python(5)
obj.function()



class Hello(Python):
    def __init__(self):
        Python.__init__(self, 5)

    def main(self):
        print("In main method")
        print(self.i)
       # print(self.__j)  # this will show error


obj2 = Hello()
obj2.main()
