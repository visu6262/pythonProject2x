#palindrom
org_name = "1221"
rev_name = ""
for c in org_name:
    rev_name = c + rev_name
print(rev_name)
if rev_name == org_name:
    print("palindrom")
else:
    print("not palindrom")
print("org_name:",org_name)
print("rev_name:",rev_name)