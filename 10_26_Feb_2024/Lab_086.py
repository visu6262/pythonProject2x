class Car():
    name=""
    model=None
    make_com=None

    def __init__(self,s_name,s_model,s_make_com):
        self.name=s_name
        self.model=s_model
        self.make_com=s_make_com

    def car_display(self):
        print(self.name,"-> car driving \n",self.model,"-> car model\n",self.make_com,"->car making companey")

visu=Car("visu","2025","Honda")
visu.car_display()
print("--------------")
komali=Car("komali","2025","Honda")
komali.car_display()
