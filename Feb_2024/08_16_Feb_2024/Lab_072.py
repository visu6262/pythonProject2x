# dict
# A Python dictionary is a collection of key-value pairs that are ordered,
# changeable, and do not allow duplicates.
# You can create a dictionary by using curly brackets {} or the dict() constructor.
my_dict={"head":"father","nhead":"mother","child1":"boy","child2":"girl"}
print(type(my_dict))
print(my_dict)
print(my_dict.keys(),my_dict.values())
for k,v in my_dict.items():
    print(k,"->",v)