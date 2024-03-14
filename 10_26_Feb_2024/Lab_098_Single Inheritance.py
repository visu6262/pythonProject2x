class Numbers_info():
    def ont_to_five(self):
        print("printing 1 2 3 4 5")

    def six_to_ten(self):
        print("printing 6 7 8 9 10")
class Alphanumaric(Numbers_info):
    def atoz(self):
        print("a b c ....upto z")

per1=Numbers_info()
per1.ont_to_five()
per1.six_to_ten()
print("------------")
per2=Alphanumaric()
per2.ont_to_five()
per2.six_to_ten()
per2.atoz()