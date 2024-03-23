# set is unordered data structure it's must be unique items and immutable it's denote by {}

a=2
set_a={3,2,'hello',a}
print(type(set_a))
print(set_a)

# create a empty set 
set_b=set()
print(type(set_b))

# Converting the set
list_1=[1,2,3,1,2]
ouput=set(list_1)
print(type(ouput))
print(ouput)

# sets are mutable which means we can add the elements to the set
result=ouput.add(4)
print(ouput.add(6))
print(ouput)

# adding the multiple items to the set

set_1={1,4,5,6}
set_1.update([2,3])
print(set_1)

# remove the specified item from the set using discord

set_1.discard(5)
print(set_1)

# set's operations 
# clear method and length
set_b={1,2,3}
set_b.clear()
print(set_b)

print(len(set_1))
# iterating the set
for item in set_1:
    print(item)
# mebership method
    
output_1=11 in set_1
print(output_1)

# update the values in the set we using list and tuple, set methods

input_a={'Ball'}
input_a.update(['apple'])
input_a.update({'cat'})
input_a.update(('dog',))
print(input_a)