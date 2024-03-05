# Filter
# it can filter the items from the list based on the logic
# return less number of items

# mylist_1=[1,2,3,4,5,6,7,8,9]
#
# aaa=list(filter(lambda num:num%2==0,mylist_1))
# print(aaa)
"""------------------------------------"""
#
# mylist_1=[1,2,3,4,5,6,7,8,9]
# def even(num):
#     return num%2==0
# def odd(num):
#     return num%2!=0
#
# aaa=list(filter(even,mylist_1))
# bbb=list(filter(odd,mylist_1))
# print(aaa)
# print(bbb)

"""-------------------------------"""

mylist_1=[1,2,3,4,5,6,7,8,9]
# def even(num):
#     return num%2==0

even_lam=lambda num:num%2==0

aaa=list(filter(even_lam,mylist_1))
print(aaa)