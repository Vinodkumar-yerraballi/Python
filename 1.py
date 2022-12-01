#Data Structure and algorithms
# fristly we create a list for weekly prices of an apple
apple_price=[250,740,555,444,550,980,920]
# each one repesently each day price start with sunday ends with saturaday
# if you want know the monday price the the code is below
# we indexing the elements the element start with 0 at the first element
print(apple_price[1])
# when we find the staturday price then the code below
print(apple_price[-1])
# we create the same method in dictiornarys
apple_price_dict={
    "sunday":250,
    "monday":740,
    "tuseday":555,
    "wendsday":444,
    "thursday":550,
    "friday":980,
    "staturday":920,
}
#finding the wendsday price
print(apple_price_dict["wendsday"])
print(apple_price_dict["staturday"])