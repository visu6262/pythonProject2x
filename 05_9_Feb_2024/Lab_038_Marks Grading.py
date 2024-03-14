# Write a program that calculates and displays the letter grade for a given numerical score
#  (e.g., A, B, C, D, or F) based on the following grading scale:
#  input- score- 89
#  output- B
#  A: 90-100
#  B: 80-89
#  C: 70-79
#  D: 60-69
#  F: 0-59
#  If, elif, else
scale = int(input("Enter scale of marks:"))
if 100 >= scale >= 90:
    print("u r grade is A")
elif 89 >= scale >= 80:
    print("u r grade is B")
elif 79 >= scale >= 70:
    print("u r grade is c")
elif 69 >= scale >= 60:
    print("u r grade is D")
elif 59 >= scale >= 0:
    print("u r grade is E")
else:
    print("in valied input")
