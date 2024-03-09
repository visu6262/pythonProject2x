class Phonne_number():
    # phone=""
    def __init(self,number):
        self.num=number

    def allnumber(self):
        if (self.num <0 and self.num >=10):
            print("enter number is 0 to 10 between")
        else:
            print("enter number is not between 0 to 10")
    def len_phone(self):
        if len(self.num) == 10:
            print("u r enter phone is ok ")
        else:
            print("u r enter phone invalied")

visu=Phonne_number()
visu.mun=9087654321

visu.allnumber()
visu.len_phone()