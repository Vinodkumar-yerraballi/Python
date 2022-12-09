print('hello world')
print('hi\nhow are you') 
print('good morning\n\t welcome to heaven')
print('he\'s man with power')
a=[1,2,4,5,6,7,8,9]
def find_min(number):
    for i in range(len(number)):
        b=min(number)
        break
print("The min values is ",find_min(a))
def find_max():
    for i in range(len(a)):
        print(max(a))
        break
    return
print("The max values is",find_max())
d=[i for i in range(10) if i%2==0]
print(d)
    

n=int(input("enter a nuber"))
if n%2==0:
    print("The number is even")
# if n in range(2,5):
#     print("Not weird")
# if n in range(5,10):
#     print("Not weird")
else:
    print("The number is odd")





