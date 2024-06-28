# write the program to check the number between 50 to 100 and first number equal to 7 return to true

# we take the first number from the user
user_input=int(input())
# convert the user input to a string
string=str(user_input)

# condition if the number is greater than 50 and less than 100
condition=(user_input > 50 and user_input < 100)

print(condition or string[0]=='7')