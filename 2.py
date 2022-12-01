# time = a*b + c
# rule 1. keep the fastest items
# rule 2. drop the constant it mean drop c
def get_squred_number(numbers):
    squred_number=[]
    for n in numbers:
        squred_number.append(n*n)
    return squred_number
numbers=[2,5,8,9]
print(get_squred_number(numbers))

def find_first_pie(prices,pie,index):
    pe=prices[index] / pie[index]
    return pe


# fing the duplicates in the list
list_duplicates=[2,3,2,3,4,5,7,5,3,7,9,9,6,3,2,4,6]
for i in range(len(list_duplicates)):
    for j in range(i+1, len(list_duplicates)):
        if list_duplicates[i]==list_duplicates[j]:
            print(list_duplicates[i])
            break
list_1=[1,2,3,4,2]
dupliccate=None
for i in range(len(list_1)):
    for j in range(i+1,len(list_1)):
        if list_1[i]==list_1[j]:
            dupliccate=list_1[i]
            break
for i in range(len(list_1)):
    if list_1[i]==dupliccate:
        print(i)

def get_squered(number):
    sq_number=[]
    #create a loop for itertion to the each elements
    for n in number:
        sq_number.append(n*n)
    return sq_number
numbers_1=[3,6,7]
print(get_squered(numbers_1))
