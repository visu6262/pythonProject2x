# useing map()
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def square_list(list_num):
#     return list_num ** 2
#
# qqq=list(map(square_list,my_list))
# print(qqq)

"""-----------------------------"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import math
def square_list(list_num):
    return math.pow(list_num,2)

qqq=list(map(square_list,my_list))
print(qqq)
