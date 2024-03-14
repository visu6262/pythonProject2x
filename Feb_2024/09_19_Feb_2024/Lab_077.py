# using instance in calss
class school():
    def ukg(self): # instancemethod declarationn
        print("this is ukg calss students")

    @staticmethod ## staticmethod declarationn
    def lkg():
        print("this is lkg class")

    def first(self):
        print("this is first class")

school.lkg() # staticmethod calling by useing direct class name with method name

sc=school()
sc.ukg()
sc.lkg()
sc.first()
