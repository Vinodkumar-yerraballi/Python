# Slicing concept
# Negative slicing
list_a=[1,2,3,4,5,6,7,8]
output_a=list_a[-1]
print(output_a)  # output 8
print(list_a[-4])  # output 5 
# slicing
print(list_a[-3:-1:1]) # output [6,7]
print(list_a[-7:-3]) # output [2, 3, 4, 5]
print(list_a[-7:-3:2]) # output [2,4]

# Extanding sliceing

# code for the extand slicing function variables[start:end:negatistep means decriment by one] start >end
nums=[5,4,3,2,1]
output=nums[4:2:-1]
print(output) # output [1,2]

# if start number less then the oputput none

nums_1=[1,2,3,4,5]
print(nums_1[2:4:-1])  # output []
# we must start indexing greater than end number

# Reverse the slice
nums_2=[5,4,3,2,1,0]
print(nums[::-1])  # output [0,1,2,3,4,5]


# index and slice in stings
sentece="Programming"
print(sentece[-4:-1]) #output  min
print(sentece[6:0:-2]) #output mro
print(sentece[6:0:-1]) # output margor


# Question and answer
list_a=input().split(",")
list_b=input().split(",")
len_of_list_a=len(list_a)
n=len_of_list_a-1

for i in range(len_of_list_a):
    num_1=list_a[i]
    num_2=list_b[i]
    result=str(num_1)+ " " +str(num_2)
    print(result)