# set{}
set1={1,2,3,4,5,5,5}
print(type(set1))
print(set1)
print(len(set1))



set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

set3=set1.union(set2)
print(set3) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

set3=set1.intersection(set2)
print(set3) #{4, 5, 6}

set3=set1.difference(set2)
print(set3) #{1, 2, 3}

set3=set2.difference(set1)
print(set3) #{8, 9, 7}

set3=set1.issubset(set2)
print(set3) #False

set3=set2.issubset(set1)
print(set3) #False

set1={1,2,3,4,5,6,7}
set2={5,6,7}

set3=set1.issubset(set2)
print(set3) #False

set3=set2.issubset(set1)
print(set3) #True