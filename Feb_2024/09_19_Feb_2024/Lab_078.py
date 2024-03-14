# staticmethod and instancemethod

class A():
    @staticmethod
    def one(self,name):
        print("this is static method ",name)

    def two(self):
        print("this is instacne method")

A.one(11,"visu")
result=A()
result.one(2,222)
result.two()
