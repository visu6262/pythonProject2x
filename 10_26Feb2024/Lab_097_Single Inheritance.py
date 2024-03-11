class Father():
    def home(self):
        print("Father has one 2 BHK flat")
    def car(self):
        print("this is father SUV car")
class Son(Father):
    def bike(self):
        print("this is son Honda Bike")

sonobj=Son()
sonobj.home()
sonobj.car()
sonobj.bike()
print("------------")
hema=Son()
hema.home()
hema.car()
hema.bike()

