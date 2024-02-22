# Fibonaci
a = 0
b = 1
while a < 10:
    print(a, end="|")
    a, b = b, a + b
"""------------------"""
print("\ntype 2 -----------")

x = int(input("Enter fibonaci up to number:"))
a = 0
b = 1
if x <= 0:
    print("plz enter +ve numbers")
else:
    while a < x:
        print(a, end="|")
        a, b = b, a + b