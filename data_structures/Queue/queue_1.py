# Lets create empty list
stock_price=[]
stock_price.insert(0,131.10)
stock_price.insert(1,131.10)
stock_price.insert(2,145)
print(stock_price)
print(stock_price.pop())
print(stock_price.pop())
from collections import deque
d=deque()
d.appendleft(45)
d.appendleft(65)
d.appendleft(99)
print(d)
print(d.pop())
print(d.pop())
orders = ['pizza','samosa','pasta','biryani','burger']
import threading
import time

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

food_order_queue = Queue()

def place_orders(orders):
    for order in orders:
        print(order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)
def serve_orders():
    time.sleep(1)
    while True:
        
        oreder=food_order_queue.dequeue()
        print(oreder)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)
    t1.start()
    t2.start()