num1 = int(input("1 st number:"))
num2 = int(input("2 st number:"))
num3 = int(input("3 st number:"))

# num4=max(num1,num2,num3)
# print("big number is:",num4)

print("-------------")
print("the max numbe is:")
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)