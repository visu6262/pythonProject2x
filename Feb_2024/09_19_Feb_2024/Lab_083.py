class cal():
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def dev(self, a, b):
        return a / b


a = float(input("enter a value:"))
b = float(input("enter b value:"))


result = cal()

out_add = result.add(a, b)
print(float(out_add))

out_sub = result.sub(a, b)
print(out_sub)

out_mul = result.mul(a, b)
print(out_mul)

out_dev = result.dev(a, b)
print(out_dev)
