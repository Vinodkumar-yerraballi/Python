# Write the code to find the greater element in the two numbers
# we take the two elements from the users

user_1_input=int(input())
user_2_input=int(input())
if user_1_input>user_2_input:
    print("user_1 is bigger elemenet than user_2",user_1_input)
else:
    print('user_2 is bigger elemenet than user_1',user_2_input)

# Write the masking code to the user input
# example user input: "vinod"
# output:"v***d"
    
user=input()
print(user[0],'*' *(len(user)-2),user[-1:])

# Question 3
'''
write  a code to check the if the two digits numer is greater than 25 and if the first digit is greater 
than second digit print the true
'''

# take the input from the user

user_input=int(input())

# we convert the number into string format
string_format=str(user_input)
# we take the first digit and convert into number format
first_digit=int(string_format[0])
# same also for the second digit
second_digit=int(string_format[1])

# apply for the condition
if user_input > 25:
    if first_digit > second_digit:
        print(True)
else:
    print(False)