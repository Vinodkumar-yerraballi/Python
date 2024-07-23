'''
Write a program to two numbers the input is taken from the user
A and B. if the A and b equal to the or less then equal to 1000
and B greater than 500 prints the pair otherwise prints not pair

'''

# userinputs 
A=int(input())
B=int(input())

# Condition
condition=(A<=1000 and B<=1000)
# If condition
if condition==True or B>500:
    print('pair')
else:
    print('Not pair')
