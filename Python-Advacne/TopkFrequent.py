#To find the Top freakent element in the given list
from collections import Counter
import heapq

#define a function to find the repeting the frequence
def TopKELements(arr,k):
    #write a condition if the k values eqal to arr which mean if the set contai 4 elements and k will be 4 it the element not repeatd at the time the condtion retun to the arr
    if k==len(arr):
        return set(arr)
    #define the counter and passing through the array
    count=Counter(arr)
    print(count)
    #this function retun the find the values frequently used in the array
    return heapq.nlargest(k,count.keys(),key=count.get)






arr=[1,1,1,1,2,2,2,2,4,4,4,4,5,5,5,5,8]
k=4
#Calling the function
result=TopKELements(arr,k)
print("The top k element in the list",result)