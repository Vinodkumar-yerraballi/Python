# Write the program to the palindrome in the numbers

n=int(input("Enter the number of the program"))

# store the input into temporary variables
temp=n
output=0

# apply the while condition 
while (n>0):
    # we divide the numbers by 10
    digit=n % 10
    output= output *10+ digit
    n = n // 10

if (temp==output):
    print("It's palindrome number")
else:
    print('It/s not palindrome number')

