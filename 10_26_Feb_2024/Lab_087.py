class Car():
    name=None
    model=None
    make_com=None

    def car_display(self):
        print(self.name,"-> car driving \n",self.model,"-> car model\n",self.make_com,"->car making companey")

x=input("enter Driver name:")
y=input("enter car modal:")
z=input("enter Car making com name:")


visu=Car()
visu.name=x
visu.model=y
visu.make_com=z
visu.car_display()
