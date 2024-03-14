
my_tuple1=("viswanath","komali","gagana","harvin")
my_tuple2=(111,222,333,444)
print(my_tuple1)
print(type(my_tuple1))
print(my_tuple1[0])
print(my_tuple1[1])
print(my_tuple1[2])
print(my_tuple1[3])
add_tuple=my_tuple1,my_tuple2
print(add_tuple)
print(add_tuple[0][0])
print(add_tuple[0][-1])
print(add_tuple[1][0])
print(add_tuple[1][-1])
con_tuple=my_tuple1+my_tuple2
print(con_tuple)

my_list=list(my_tuple1)
print(my_list)
my_list.append(999)
print(my_list)



