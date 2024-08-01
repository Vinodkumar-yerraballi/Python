

# Let's find the minimum and maximum element  in the list

# list
arr=[1,2,3,4,5,]

# initialize the maximum and minimum element

maximum=arr[0]
minimum=arr[1]

# condition

for i in arr:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print(f'The maximum value in the list {maximum}, the minimum value in the list {minimum}')