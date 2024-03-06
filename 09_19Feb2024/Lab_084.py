class CAR():
    colour = None
    modal = None

    def mod_col(self):
        print("You are car colour ", self.colour, "and car model is:", self.modal)

x = input("enter car colour:")
y = input("enter car modal:")


a = CAR()
a.carmodal=x
a.carcolour=y
a.mod_col()
