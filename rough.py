import cmath
import math
from math import sin,cos
def square_root(a,b):
    return a**2+b**2+2*a*b
print(square_root(3,5))
def score(a,b,c):
    d=(b**2)-(4*a*c)
    sol1=(-b-cmath.sqrt(d))/(2*a)
    sol2=(-b+cmath.sqrt(d))/(2*a)
    return print('The solution are {0} and {1}'.format(sol1,sol2))

print(score(1,2,4))
def qube_formula(a,b):
    return a**3+b**3+3*a*b*(a+b)
print(qube_formula(2,4))
def qube_formual_minise(a,b):
    return a**3-b**3-3*a*b*(a-b)
print(qube_formual_minise(4,5))
