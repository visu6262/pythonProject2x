# Identity Operators : is , is not
# it will check given value is same memory location or not
a=2
b=5
print(a is b)
print(a is not b)

a=b=6
print(a is b)
print(a is not b)

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)