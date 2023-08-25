matrix=[[0,0,0],
        [0,0,0],
        [0,0,0],]
print("   a  b  c")
for i,row in enumerate(matrix):
    print(i,row)
print("-"*20)
# using index slicing change the Some changes
matrix[0][0]=1
matrix[1][1]=1
matrix[2][2]=1
print("   a  b  c")
for col,row in enumerate(matrix):
    print(col,row)

# Using the loop print the names of the users in the
name=input("Enter the name of the user ")
for i in range(len(name)+1):
    print(name[:i])
    print('----------------------------------------------------------------')
    print(name[i:])
