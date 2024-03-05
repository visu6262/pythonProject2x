# def say_hello(): # without argument
#     print("hello all")
# say_hello()
#
# """-------------"""
# print("type2___________")
# def say_hello(name): #argument: 'name' is passing
#     print("hi hello",name)
# say_hello("ram")
# """--------------------"""
# print("type3___________")
# def say_hello(name="visu"): #argument with defalt value: 'name=visu' is passing
#     print("hi hello",name)
# say_hello("ram")
# say_hello()
# """---------------------"""
# print("type4___________")
# def say_hello(name="visu",age=33):  #multiple argumment passing with defalt valus
#     print("hello",name,age)
# say_hello("komali",27)
# say_hello()
# """--------------------"""
# print("type5___________")
x=input("Enter u r name:")
y=input("Enter u r age:")
def say_hello(name="visu",age=33): #argument with defalt value: 'name=visu' is passing
    print("hi hello",name,"and u r age is:",age)
p=say_hello(x,y)