class Car_info():
    def information(self):
        print("thes car information details")

class Eng_info(Car_info):
    def eng(self):
        print("this car eng type is V6")

class color_info(Car_info):
    def color(self):
        print("this car colour is blue")

class alldetails_car(Eng_info,color_info):
    def display_car(self):
        print("all details of car")

visu=alldetails_car()
visu.display_car()
visu.color()
visu.eng()
visu.information()