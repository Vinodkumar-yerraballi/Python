class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singleLinkedlist :
    def __init__(self):
        self.head=None
    #create  a function
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
               print(temp.data,"--->",end=" ")
               temp=temp.next

#create a object for the single linked list    
L=singleLinkedlist()
n=Node(10)
L.head=n  # type: ignore
n1=Node(20)
L.head.next=n1  # type: ignore
n2=Node(300)
n1.next=n2  # type: ignore
n3=Node(400)
n2.next=n3  # type: ignore
L.display()