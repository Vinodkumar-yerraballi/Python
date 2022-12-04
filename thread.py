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

    def front(self):
        return self.buffer[-1]
    
def producer_binaray_number(n):
    numbers_enq=Queue()
    numbers_enq.enqueue("1")
    for i in range(n):
        fornt=numbers_enq.front()
        print("values",fornt)
        numbers_enq.enqueue(fornt+ "0")
        numbers_enq.enqueue(fornt + "1")
        numbers_enq.dequeue()

if __name__ == "__main__":
    producer_binaray_number(10)


