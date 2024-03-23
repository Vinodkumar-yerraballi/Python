
# sets's operation with the first value is 

set_1={1,2,4,4}
set_2={2,5,6,7}
# what happens when the union the common values return to single values

print(set_1 | set_2)
result=set_1.union(set_2)
print(result) # output : {1,2,3,5,6,7}

# intersection
# instersection will return only common values in the two sets

ouptut=set_1 & set_2
set_1={1,2,3,4}
set_2={5,2,3,7}
print(set_1.intersection(set_2))  # output : {2,3}
print(ouptut)  # output : {2}

# difference operation

# a set contains the all elements except the first set but not the second set
# which meanns the differnece element is removed and the element is deleted first set and print the remaing element
input_1 = {1,2,4}
input_2 = {2,5,6}
print(input_1 - input_2) # output : {1,4}
print(input_1.difference(input_2)) # output : {1,4}  it print the after the common element print first element set

# symmetric difference operation
# a set contains the all elements except the first set but not the second set
print(input_1 ^input_2)  # output : {1, 4, 5, 6}
print(input_1.symmetric_difference(input_2)) # output : {1, 4, 5, 6} # it remove the common elements

# set comparison
# issubset 
# if the common elements are in the second set return true
input_a={1,2,3,4}
input_b={1,2}
input_c={5,6}
print(input_b.issubset(input_a)) # output : True
print(input_c.issubset(input_a)) # output : False

# issuperset
# if the common elements are in the first set with second set return true
print(input_a.issuperset(input_b)) # output : True

# disjoint set
# if you have common values in the set return to false otherwise return true

a={1,2,3}
b={4,5,6}
c={1,2,4}
print(a.isdisjoint(b)) # output: True
print(a.isdisjoint(c)) # output: False