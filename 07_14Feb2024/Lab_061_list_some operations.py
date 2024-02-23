# list- some operations
my_list = [1, 9, 3]
print(my_list)
# indexing
print("elemant index 0 is", my_list[0])
# changing a elemant
my_list[1] = "a"
print((my_list))
# adding elemant in last
my_list.append(2)
print(my_list)
#addind elemants in last with bulk
my_list.extend([10,20])
print(my_list)
#adding elemants with spacific index plase
my_list.insert(1,100)
print(my_list)
# removeing elemants from list
my_list.remove("a")
print(my_list)
#copy of the list
my_listcopy = my_list.copy()
print("my_list",my_list)
print("my_listcopy",my_listcopy)
#sort assending
my_list.sort()
print("after sort assending",my_list)
#sort dessending
my_list.reverse()
print("after sort dessending",my_list)
#clear
my_list.clear()
print("my_list",my_list)
print("my_listcopy",my_listcopy)


