class School_info:
    def dasic(self):
        print("thie is basic school information")
        print("kindergarden school infor")

class Upto_tenth(School_info):
    def first(self):
        print("this 1st class information")
    def second(self):
        print("this 2nd class information")
    def threed_to_6(self):
        print("this up to 6th class information")

jai=School_info()
jai.dasic()
print("------------")
raju=Upto_tenth()
raju.dasic()
raju.first()
raju.second()
raju.threed_to_6()