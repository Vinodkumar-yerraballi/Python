class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("the linked is empty")
        else:
            itr=self.head
            while itr:
                print(itr.data,"--->",end= " ")
                itr=itr.next
l=singlelist()
n=Node("apple")
l.head=n
n1=Node("banna")
l.head.next=n1
n2=Node("Chippa")
n1.next=n2
l.display()

            


    