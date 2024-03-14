class CAR():
    name = color = modal = engine = speed = None

    def who_is_drving(self):
        print("im drving this car =>", self.name)

    def c_color(self):
        print("this car colour is ->", self.color)

    def c_modal(self):
        print("this car modal is ->", self.modal)

    def eng(self):
        print("car engine is ->", self.engine)

    def c_speed(self):
        print('this car max speed ->', self.speed)



ram = CAR()
ram.name = "Ram"
ram.color = "blue"
ram.modal = 2024
ram.engine = "2Litar"
ram.speed = 150

ram.who_is_drving()
ram.c_color()
ram.eng()
ram.c_speed()
ram.c_modal()
