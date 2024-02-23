# str = input("Enter name witch u want to revers:")

def revers_str(str):
    last_to_first = " "
    for c in str:
        last_to_first = c + last_to_first
    print(last_to_first)
    return last_to_first

original_str =input("Enter name witch u want to revers:")
original_str = original_str.lower()
aaa = revers_str(original_str)
# print(aaa)
if aaa == original_str:
    print("palindrom")
else:
    print("not palindrom")

print("aaa         :", aaa)
print("original_str:", original_str)