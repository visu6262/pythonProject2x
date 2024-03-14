# Create a program that determines whether a given year is a leap year.

year = int(input("Enter year:"))
if year % 4 == 0 and (year % 400 ==0 or year % 100 !=0):
    print("given year is Leap year")
else:
    print("given year is NOT Leap year")

# a=2024
# print(a%4 == 0)
# print(a%400 == 0)
# print(a%100 != 0)