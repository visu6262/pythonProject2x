# useing map()
import math


def sq_num(num):
    return math.sqrt(num)


my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# sss =list(map(sq_num, my_list))
# print(sss)

print(list(map(sq_num, my_list)))

