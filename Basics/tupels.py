# Tuples is mutubule data structure

a=(1,2,3,4,5,6)
print(type(a))

# if you want convert the elements tuple you can write comma ofter the elements

b=()
print(type(b))

c=(1,)
print(type(c))

# operations of the tuple
# len of the tuple

print(len(a))

# slicing  methods

print(a[1:3])

# iterators
for items in a:
    print(items)

# if you convert the sequence to a tuple we can do processing
    
name='Vinod'
print(tuple(name))

# and range functions

output=tuple(range(5))
print(output)

# membership checking
result_1= 7 in a
result_2=5 in a
print(result_1) # output  : False
print(result_2) # output  : True

# unpacking 
# sequence number is assinged to the directly to the variable
tuple_1=('a', 'b', 'c')
(a_1,b_1,c_1)=tuple_1
print(a_1) # output : a
print(b_1) # output : b
print(c_1) # output : c
# we can do this with list also
tuple_2=['a', 'b', 'c']
(a_2,b_2,c_2)=tuple_2
print(a_2) # output : a
print(b_2) # output : b
print(c_2) # output : c

#add the number and multiplication
def add_multplication(a,b):
    add_num= a+b
    mult_num = a*b
    return add_num,mult_num
x,y=add_multplication(4,5)
print(x) # output :9
print(y) # output :20


# coding challenge

str_a=int()
a=str_a.split(",")
i=0

for items in a:
    a[i]=items
    i += 1
print(tuple(a)) # output : ('1', '2', '3')