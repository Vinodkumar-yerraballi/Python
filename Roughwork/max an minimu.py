# find the maximum and minimum sum in the given array

def min_max_sum(arr):
    total_sum=sum(arr)
    #maximum  value
    maximum=0
    #minimum value
    minimum=float('inf')
    for num in arr:
        current_sum=total_sum-num
        if current_sum>maximum:
            maximum=current_sum
        if current_sum<minimum:
            minimum=current_sum
    return minimum,maximum


def MinMaxSum(arr):
    arr.sort()
    print(sum(arr[0:4]),sum(arr[1:5]))

arr=[1,2,3,4,5]

print(min_max_sum(arr))
print(MinMaxSum(arr))

