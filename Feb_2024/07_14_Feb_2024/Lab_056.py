def make_pizza(*topings):
    print(topings)
    for top in topings:
        print(top)
make_pizza("onians","tomato")
make_pizza("onians","tomato","carreat")
make_pizza("onians","tomato","carreat","butter")
visu=make_pizza("onians","tomato","carreat","butter","sass","sweetcorn")

"""---------------------------"""
print("type 2_____________")
def make_pizza(*topings,base):
    print(topings,"Base is like:",base)
    for top in topings:
        print(top)
    print("Base is:",base)

visu=make_pizza("1 Onians","tomato","carreat","butter","sass","sweetconr",base="thin")
