import threading
import time

def square_number(numbers):
    for n in numbers:
        print("squared_number",n*n)
number=[2,3,4,5]
square_number(number)

def cube_number(numbers):
    for n in numbers:
        print("cube_number",n*n*n)
number1=[2,3,4,5]
cube_number(number1)
def sleep(i):
    print("doctor",i)
    time.sleep(5)
    print("sleep",i)

for n in range(10):
    th=threading.Thread(target=sleep,args=(n,))
    th.start()
    print(threading.active_count())

li=["apple","banna","cat"]
for i in range(len(li)):
    stock=[]
    stock.append(li)
    print(stock)