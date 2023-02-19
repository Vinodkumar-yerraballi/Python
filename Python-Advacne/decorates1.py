def polynomial_creator(a,b,c):
    def ploynmial(x):
        return a*x+b*x+c
    return ploynmial

print(polynomial_creator(2,4,5))

def polynomial_creator(*coffiencts):
    def polynomial(x):
        for index,coeff in enumerate(coffiencts[::-1]):
            result += coeff * x **index
            return result
        return polynomial
coff=[1,2,3,4,5]
print(polynomial_creator(4))
        

def polynomial_creator(*coeff):
    def polynomial(x):
        res=coeff[0]
        for i in range(1,len(coeff)):
            res=res*x+coeff[i]
        return res
    return polynomial

print(polynomial_creator(2))
list_1=[1,2,3,4,5,6]
for index,coeff in enumerate(list_1[::-1]):
    print(index,coeff)


def our_decorator(func):
    def function_wrapper(x):
        print("berore alling"+func._name_)
        func(x)
        print("Ater alling"+func._name_)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi" +str(x))


def argument_test_natural_number(f):
    def helper(x):
        if type(x)==int and x>0:
            return f(x)
        else:
            raise Exception ("Argumernt is not ")
    return helper
@argument_test_natural_number
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
for i in range(1,10):
    print(i,factorial(i))