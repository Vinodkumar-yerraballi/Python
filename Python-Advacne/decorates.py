def sucess(x):
    return x+1
print(sucess(10))
def f():
    def g():
        print('Hi how are you')
        print("Welcome to my world")

    print('There is very huge')
    print('Let celeabrate it')
    g()

print(f())

def temparature(t):
    def celisus2fraction(x):
        return 9*x/5+32
    result="it's" + str(celisus2fraction(t)) + 'degree'
    return result
print(temparature(7))

def factional(n):
    if n==0:
        return 1
    else:
        return n*factional(n-1)

print(factional(4))

def fractional(n):
    if type(n)==int and n>=0:
        if n==0:
            return 1
        else:
            return n * fractional(n-1)
    else:
        raise TypeError("n has to result")

def factoial(n):
    def inner_factoria(n):
        if n==0:
            print('Return {}'.format(n))
            return 1
        else:
            ret_value= n* inner_factoria(n-1)
            print('returning {}'.format(ret_value))
        return ret_value
    if type(n)==int and n>=0:
        return inner_factoria
    else:
        raise TypeError("n has no result")
