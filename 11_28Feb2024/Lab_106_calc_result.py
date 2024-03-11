import Lab_105_calc

addobj=Lab_105_calc.add(10,13)
print(addobj)

mulobj=Lab_105_calc.mul(10,15)
print(mulobj)

subobj=Lab_105_calc.sub(20,5)
print(subobj)

print("----------------")

from Lab_105_calc import add,mul,sub
addobj=add(10,30)
print(addobj)

mulobj=mul(10,30)
print(mulobj)

subobj=sub(30,10)
print(subobj)

print("----------------")

from Lab_105_calc import *
addobj=add(10,30)
print(addobj)

mulobj=mul(10,17)
print(mulobj)

subobj=sub(30,20)
print(subobj)
