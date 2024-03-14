import Lab_107_class
import Lab_109_class_calculater
output= Lab_107_class.even_or_odd()
output.num(10)
output.num(5)
print("-----------------")
result= Lab_109_class_calculater.calc()
print(result.add())
print(result.sub())
print(result.mul())

print("-----------------")
from Lab_107_class import even_or_odd
result=even_or_odd()
result.num(5)
from Lab_109_class_calculater import calc
result=calc()
print(result.add())
print(result.sub())
print(result.mul())
