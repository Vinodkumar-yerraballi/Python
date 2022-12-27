class Queue:
    def __init__(self,data):
        self.data=data
        self.fornt=0
        self.rear =0
        self.arr=[None]

    #How to add the elements in the queue
    def add_element(self,val):
        if self.rear==self.data:
            print("The Queue is full")
        else:
            self.arr[self.rear]=val
            self.rear=self.rear+1

    #Let's delete the element in the queue
            
    def delete_element(self):
        if self.rear==self.fornt:
            print("The Queue is empty")
        else:
            print("The delete element is ", self.arr[self.fornt])
            self.fornt=self.fornt+1


if __name__=="__main__":
    list=[1,3,45,5]
    theque=Queue(list)
    list=[1,2,3,5]
    theque.add_element(list)
    element=3
    print(list)
