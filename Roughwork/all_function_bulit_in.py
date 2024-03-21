# Write the lambda,filter,reduce,map function

# both functions are called anonymously function it's simple and single line expression

# apply the lambda function
from functools import reduce

list_a=[3,4,2,6,8,10,12]
print(list_a)
# using the lambda function print the square roots of the given list
list_1_output=list(map(lambda  x: x**2,list_a))
print(list_1_output)

# filter function used to filter the given list
# in the given list write the print the even numbers

output_list_a=list(filter(lambda x: x%2==0,list_a))
print(output_list_a)

# reduce function used to reduce the list and sum of the given list

reduce_output_list_a=reduce(lambda x,y: x+y,output_list_a)
print(reduce_output_list_a)
