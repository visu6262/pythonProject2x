class Person():
    name = None
    age = None
    def dis_name(self):
        # self.name = name
        print("You are name is : "+self.name)

    def dis_age(self):
        # self.age = age
        print("You are age is :"+self.age)


# harvin=Person()
# harvin.dis_name("Harvin")
# harvin.dis_age("4")

visu=Person()
visu.name="visu"
visu.age="33"
visu.dis_name()
visu.dis_age()