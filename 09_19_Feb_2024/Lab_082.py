class cal():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def dev(self,a,b):
        return a/b
result=cal()

out_add=result.add(10,20)
print(out_add)

out_sub=result.sub(20,10)
print(out_sub)

out_mul=result.mul(10,20)
print(out_mul)

out_dev=result.dev(10,20)
print(out_dev)
