# write a programm to find the greates element in the given three integers
# let's take the input from the users
a=int(input())
b=int(input())
c=int(input())

# Let's apply the condition
# check the a is greater than b and c
if (a >b) and (a >c):
    print(a)
# Second time we check the b is greate and the c is
else:
    if (b>c):
        print(b)
    else:
        print(c)
# Second question 
'''
Write a program to find the weathe element is divisible by 5 and 10
if number is divisible by 10 return to divisible by 10 and 
it's divisible by 5 return to divisible by 5
when the two condition is failed return it's not divisible by both 5 and 10
'''

# take the input from the user
user_input=int(input())

# check the condition one if the element is divisible by 10
if (user_input %10 ==0):
    print('divisible by 10')
elif (user_input %5 ==0):
    print('divisible by 5')
else:
    print('Not divisible by 10 and 5')