#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Find the sum of the subarrays
def find_sum_of_subarrys(arr,sum_value):
    # we can store the values in the dictionary formate
    dict_1={}
    current_sum=0
    # looping the array
    for i in range(len(arr)):
        current_sum=current_sum+arr[i]
        if current_sum==sum_value:
            break 
        if current_sum-sum_value in dict_1:
            print(dict_1[current_sum-sum_value]+1 ,i)
            break
        dict_1[current_sum]=i
arr=[1,4,20,3,10,5]
sum_value=33
print(find_sum_of_subarrys(arr,sum_value))


# #### Find The Maximum Product of the subarrays

# In[2]:


# Let's find the maximum product of the subarrys
def find_maximum_product(A):
    # Write some variable to store the values
    
    current_max=A[0]
    current_min=A[0]
    previous_max=A[0]
    previous_min=A[0]
    result=A[0]
    
    for i in range(1,len(A)):
        current_max=max(previous_max*A[i] , previous_min*A[i], A[i])
        current_min=min(previous_max*A[i] , previous_min*A[i], A[i])
        result=max(current_max,result)
        previous_max=current_max
        previous_min=current_min
    return result
arry=[-6,4,-5,8,-10,0,8]
print(find_maximum_product(arry))


# ####  Print the duplicate elements in the list

# In[3]:


inputs=[10,1,2,10,20,30,20,30,5]
output=[]
for i in inputs:
    if inputs.count(i)>1 and i not in output:
        output.append(i)
print(output)
# Second methods
for i in range(len(inputs)):
    for j in range(i+1,len(inputs)):
        if inputs[i]==inputs[j] and inputs[i] not in output:
            output.append(j)
print(output)


# #####  Dictionary problems

# In[4]:


names=['krish naik','Elon musk','Modi','virat']
profe=['youtuber','businessman','prime minister','circketer']
my_dict={}
for (key,value) in zip(names,profe):
    my_dict[key]=value
print(my_dict)
my_dict_1={
    "Spider":"Photograper",
    "iron" :"Scientist",
    "Super" :"Know"
}
# Without items method we can't display the value methods
output={key+"man":value for (key,value) in my_dict_1.items()}
print(output)


# In[12]:


my_dict_1={
    "Spider":"Photograper",
    "iron" :"Scientist",
    "Super" :"Know"
}
output={(key+"man" if key !='Spider' else "Batman"):
        (value if value !='Photograper'  else "Journalist") 
        for (key,value) in my_dict_1.items()}
print(output)


# In[ ]:




