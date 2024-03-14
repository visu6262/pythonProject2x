# protected and private in python
class students:
    def __init__(self):
        self.name = "raju"
        self._age = 22
        self.__cast = "cast_OBC"

    def age(self):
        print("You are age is",self._age)

    def cast(self):
        print("Your cast is :",self.__cast)


raju = students()
print(raju.name)
raju.age()
raju.cast()
print("-----------")
hema = students()
print(hema.name)
hema.age()
hema.cast()