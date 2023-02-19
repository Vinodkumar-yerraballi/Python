my_items=[2,4,5,6,8]
def squre(x):
    return x**2
print(list(map(squre,my_items)))
for each in map(squre,my_items):
    print("The square items",each)
val=list(map(lambda x: x**2,my_items))
print("The sqaure",val)

def square(x):
    return (x**2)
def cube(x):
    return (x**3)

func=[square,cube]
for i in range(5):
    value=map(lambda x: x(i),func)
    print(list(value))

def to_upper_case(s):
    return str(s).upper()
    def print_iter(it):
        for x in t:
            print(x,end='')
        print('Welcome')
print(list(map(to_upper_case,'abc')))
print(list(map(to_upper_case,["apple",'cat','dog'])))

list_numbers=[1,2,3,4,5]
tuple_numbers=(5,6,7,8,9)
map_iter=map(lambda x,y : x * y ,list_numbers,tuple_numbers)
print(map_iter)

r=list(range(-5,5))
result=[]
for x in r:
    if x<0:
        result.append(x)
print(result)
print(list(filter(lambda x: x<0,r)))

def funcs(var):
    letter=['a','e','i','o','u']
    if (var in letter):
        return True
    else:
        return False
sequre=['a','b','k']
fileter=filter(funcs,sequre)
print(fileter)

from functools import reduce
number=[1,2,3,4]
total=0
for num in number:
    total +=num
print(total)
def my_add(a,b):
    return a+b

print(reduce(my_add,number))