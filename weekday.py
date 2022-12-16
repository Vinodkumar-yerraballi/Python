class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def visualize(self):
        tmp=self.head
        while tmp:
            print(tmp.data, '--->',end=' ')
            tmp=tmp.next
    def Atbegineg(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def inbetween(self,midel_node,newdata):
        newnode=Node(newdata)
        if midel_node is None:
            print("No middel element")
            return
        newnode.next=midel_node.next
        midel_node.next=newnode

    # How to add the value at the end
    def Atend(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=newnode

    
    

if __name__=='__main__':
    link=Linkedlist()
    l1=Node('Mon day')
    l2=Node('Thurs day')
    l3=Node('Friday')
    link.head=l1
    link.head.next=l2
    l2.next=l3
    link.Atbegineg('Sunday')
    link.Atend('Saturday')
    link.inbetween(link.head.next,'Wendsday')
    link.inbetween(link.head.next,'Thuesday')
    link.visualize()