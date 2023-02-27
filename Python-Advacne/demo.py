def add_numbers(*numbers):
    result=0
    for num in numbers:
        result +=num
    return result
print(add_numbers(3,5))
print(add_numbers(1,2,3,4))

def myfunc(*arg):
    for argv in arg:
        print(argv)

print(myfunc('Hi','Welcome to my world','Spread','good'))

def my_function(arg1,*arg2):
    print('The first element',arg1)
    for args in arg2:
        print(args)

print(my_function('Hi','How can i help you','Do you need any help','shock the society'))

def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s" %(key,value))

print(myFun(first='vinod',mid='kumar',last='yerraballi'))


class car:
    def __init__(self,*args):
        self.speed=args[0]
        self.color=args[1]

audi=car(200,'red')
bmw=car(198,'black')
mb=car(190,'white')

print(audi.color)
print(mb.speed)