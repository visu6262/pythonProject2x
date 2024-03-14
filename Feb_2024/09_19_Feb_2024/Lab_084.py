class CAR():
    colour = None
    modal = None

    def mod_col(self):
        print("You are car colour :", self.colour,"\nand car model is:", self.modal)

x = input("enter car colour:")
y = input("enter car modal:")


a = CAR()
a.modal=x
a.colour=y
a.mod_col()
