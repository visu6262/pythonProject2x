class Grandfather():
    def agland(self):
        print("Grand father have 5 acre land")
    def gold(self):
        print("Gran father have 5 kg gold")
    def bankbalance(self):
        print("Grand father have 5 cr bank balance")

class Father(Grandfather):
    def home(self):
        print("Father has one 2 BHK flat")
    def car(self):
        print("this is father SUV car")
class Son(Father):
    def bike(self):
        print("this is son Honda Bike")


print("------------ Son Obj")
sonobj=Son()
sonobj.agland()
sonobj.gold()
sonobj.bankbalance()
sonobj.home()
sonobj.car()
sonobj.bike()
print("------------ Father Obj")
hema=Father()
hema.home()
hema.car()
hema.agland()
hema.gold()
hema.bankbalance()

