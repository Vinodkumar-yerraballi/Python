num1=int(input("Enter the number ",))
num2=int(input("Enter the number ",))

# write the code to find the largest hcf values

def find_largest_hcf(num1, num2):
    # check the number with less values
    if num1 < num2:
        smaler=num1
    else:
        smaler=num2
    # take the hcf values from the
    hcf=1
    # iterate over the values
    for i in range(1,smaler):
        if (num1 %1 ==0 and num2 %1 ==0):
            hcf=i
    return hcf 
output=find_largest_hcf(num1,num2)
print(output)