# Even and odd number find

# take the input from the user
input_1=int(input())
# if the input is divided by two
result=input_1 % 2

# and apply the condition
# when the remainder is equal to the zero return to even
if result == 0:
    print('Even')
else:
    print('Odd')