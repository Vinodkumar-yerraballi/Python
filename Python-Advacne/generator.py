def foo():
    print('[mod1] foo()')
class Foo:
    pass

def mygenartor():
    print('Firstitem')
    yield 10
    print('Second item')
    yield 20
    print('Thrid item')
    yield 30
gen=mygenartor()
while True:
    try:
        element=next(gen)
        print(element)
    except StopIteration:
        break

def getsequenve(x):
    for i in range(x):
        yield i
get=getsequenve(10)
print(get)

def fibonace(max):
    a,b=0,1
    while a< max:
        yield a
        a,b=b,a+b

fib=fibonace(10)
print(fib)