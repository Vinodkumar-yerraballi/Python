# import cmath
# import math
# from math import sin,cos
# def square_root(a,b):
#     return a**2+b**2+2*a*b
# print(square_root(3,5))
# def score(a,b,c):
#     d=(b**2)-(4*a*c)
#     sol1=(-b-cmath.sqrt(d))/(2*a)
#     sol2=(-b+cmath.sqrt(d))/(2*a)
#     return print('The solution are {0} and {1}'.format(sol1,sol2))

# print(score(1,2,4))
# def qube_formula(a,b):
#     return a**3+b**3+3*a*b*(a+b)
# print(qube_formula(2,4))
# def qube_formual_minise(a,b):
#     return a**3-b**3-3*a*b*(a-b)
# print(qube_formual_minise(4,5))
# def recursion(n):
#     if n<=1:
#         return n
#     else:
#         return(recursion(n-1)+recursion(n-2))
    
# n_items=10
# if n_items<=0:
#     print("invalid number")
# else:
#     print("fobius series")
# for i in range(n_items):
#     print(recursion(i))

# def problem(a,b):
#     value=float((a+b)*(a-b))//float((a-b))
#     return value
# print("This is apptitude problem solution",problem(2.39,1.61))

# apple=[1,2,4,4]
# def find_sum(elelments,elements_sum):
#     b=0
#     c=len(elelments)-1
#     while b< c:
#         evaluation=elelments[b]+elelments[c]
#         if evaluation==elements_sum:
# #             return True
# print("The solution of the array is",find_sum(apple,8))

ball=[1,2,3,4,5,6,7]
#Let's find the middel number
middel=(len(ball)-1)/2
print("Let's find the middle number",middel)

for i in range(len(ball)-1):
    i +=1
    print(ball[i])