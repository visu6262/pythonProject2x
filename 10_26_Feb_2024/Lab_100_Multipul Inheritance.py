class Mother():
    def gold(self):
        print("Gran father have 1 kg gold")
    def bankbalance(self):
        print("Grand father have 5 lakh bank balance")

class Father():
    def home(self):
        print("Father has one 2 BHK flat")
    def car(self):
        print("this is father SUV car")
class Son(Father,Mother):
    def bike(self):
        print("this is son Honda Bike")


print("------------ Son Obj")
Harvin=Son()
Harvin.gold()
Harvin.bankbalance()
Harvin.home()
Harvin.car()
Harvin.bike()
print("------------ Father Obj")
hema=Father()
hema.home()
hema.car()

