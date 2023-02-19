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

# Remove the dublicate in the list 
list_a=[1,2,3,2,2,1,4,5,6,5,6]
#create a empty list=[]
new_list=[]
# use loop codition
for i in list_a:
    #using the if codition for the element not in the empty list then it will be append
    if i not in new_list:
        new_list.append(i)
print(new_list)

# [new_list.append(i) for i in list_a if i not in new_list]
# print("Another method of the duplicate list",new_list)
# def remove_duplicate(a):
#     new_list=[]
#     for i in a:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# list_b=[1,1,3,3,4,5,6,6,7]
# print("The  function of the new list is ",remove_duplicate(list_b))
# languages=["Telugu","English","Hindi"]
# for i in languages:
#     print(i)
#     print("Choose Your language")
#     number=int(input("Enter your langugae number in 0-2  "))
#     if number==0:
#         print("Telugu",languages[0])
#     elif number==1:
#         print("English",languages[1])
#     else:
#         print("Hindi",languages[2])
#     break
password=1234
atm_pin=int(input("Enter pin "))
if password==atm_pin:
    print("Change your old pin")
    new_pin=int(input("Enter new pin  "))
    password=new_pin
    print(password)
    # if languages=="Telugu":
    #     print("Press 1",languages[0])
    # elif languages=="English":
    #     print("Press 2",languages[1])
    # else:
    #     print("Press 3 ",languages[2])