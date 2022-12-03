#firstly we create empty string
# the concept of the stack similary to the seaching of the website pages
stack=[]
stack.append('www.google.com')
stack.append('www.facebook.com')
stack.append('www.twitter.com')
print(stack.pop())
print(stack.pop())
print(stack.pop())
#print(stack.pop())
from collections import deque
stack1=deque()
stack1.append('www.instagram.com')
stack1.append('www.dell.com')
stack1.append('www.hp.com')
print(stack1)
print(stack1.pop())
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
def reverse_string(text):
    return text[::-1]
print(reverse_string("We will conquere COVID-19"))
