for i in [1,2,3,4,5]:
    print(i)
for j in "Hello world":
    print(j)
for k in {'x':1,'y':2}:
    print(k)

my_list=[3,4,5,6,7]
my_iter=iter(my_list)
while True:
    try:
        element=next(my_iter)
        print(element)
    except StopIteration:
        break