def sum_two(a,b):
    return a+b
p=sum_two(2,5)
print(p)
"""---------------"""
print("type2-------------")
def sum(a=1,b=1,c=1):
    return a+b+c
p=sum(1,1,1)
print(p)
p=sum()
print(p)
p=sum(a=5) #a=5 b=1 c=1
print(p) # output 7
p=sum(2,2) #a=2,b=2,c=1
print(p) #output 5
p=sum(5,5,5)
print(p)
p=sum(1.5,2.5,5.5)
print(p)
p=sum("visu","kolali","gagana")
print(p)