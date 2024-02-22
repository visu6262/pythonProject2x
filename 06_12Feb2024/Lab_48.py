# num = int(input("Enter a number: "))
# # check if the number is negative, positive or zero
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
num=5
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("The factorial of", num, "is", fact)