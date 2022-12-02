#Data Structure and algorithms
# fristly we create a list for weekly prices of an apple
apple_price=[250,740,555,444,550,980,920]
# each one repesently each day price start with sunday ends with saturaday
# if you want know the monday price the the code is below
#insert the first element 333 in  the array
apple_price.insert(2,333)
#Remove the 555 in 250 in the array
apple_price.remove(550)
# we indexing the elements the element start with 0 at the first element
print(apple_price[1])
# when we find the staturday price then the code below
print(apple_price[-1])
#find the 555 price in the array
for i in range(len(apple_price)):
    if apple_price[i]==555:
        print(i)

# we create the same method in dictiornarys
# apple_price_dict={
#     "sunday":250,
#     "monday":740,
#     "tuseday":555,
#     "wendsday":444,
#     "thursday":550,
#     "friday":980,
#     "staturday":920,
# }
#finding the wendsday price
# print(apple_price_dict["wendsday"])
# print(apple_price_dict["staturday"])
# for price in apple_price:
#     print(price)

# Exercise: Array DataStructure
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

expenses=[2200,2350,2600,2130,2190]
# 1. In Feb, how many dollars you spent extra compare to January?
for i in range(len(expenses)):
    feb=expenses[1]-expenses[0]
    print(feb)
    break
# 2. Find out your total expense in first quarter (first three months) of the year.
for i in range(len(expenses)):
    third=expenses[0]+expenses[1]+expenses[2]
    print(third)
    break
# 3. Find out if you spent exactly 2000 dollars in any month
for i in range(len(expenses)):
    if expenses[i] == 2000:
        print(i)
# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print(expenses)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3]=expenses[3]-200
print(expenses)


