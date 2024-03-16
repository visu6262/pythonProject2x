print("program started")
try:
    num1=int(input("Enter Number 1 value:"))
    num2=int(input("Enter Number 2 value:"))
    print("inprogress")
    result=num1/num2

    print(f"Result is :{result}")

except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)

print("Progrem completed")