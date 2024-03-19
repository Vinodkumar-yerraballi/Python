# Find the sum of the given list

list_1=[1,2,4]
# to find the sum of the given list go through the loops
# take the result variable is zero
result=0
for i in list_1:
    result=result+i
print(result)

# How to sum of the given two lists it's must be same length
list_a=[38,19,20,49]
list_b=[44,55,93,20]
# let's we take the empty list to store the result
output=[]
# while apply the loop system
for i in range(len(list_a)):
    output.append(list_a[i]+list_b[i])
print(output)

# second method
final_output =[x+y for x,y in zip(list_a,list_b)]
print(final_output)

# Let's find the common elements in the two lists
a=[1,2,3]
b=[1,4,6]
two_list_sum=[]
for i in a:
    for j in b:
        if i==j:
            two_list_sum.append(j)
print(two_list_sum)  # output 1