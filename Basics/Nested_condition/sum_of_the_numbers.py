# let's find the sum of the number 

def sum_of_the_number(number):
    # firstly we convert the number string 
    string = str(number)
    output = 0
    for i in string:
        integer = int(i)
        output += integer
    return output
user_input =int(input("Enter a number "))
print(sum_of_the_number(user_input))