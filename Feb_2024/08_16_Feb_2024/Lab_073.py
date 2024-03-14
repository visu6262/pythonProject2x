person = dict(name="Raj", age=25, occupation="engineer", ismale="True", phoneno="9012345678", email="abc@mail.com")

print(len(person))
print(person.get("name"))
print(person.get("age"))
print(person["name"])
print(person["age"])

result=person.keys()
print(result)

print("keys are:",person.keys())

result2=person.values()
print(result2)

print("values are:",person.values())