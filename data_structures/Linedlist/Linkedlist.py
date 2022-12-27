class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkdedList:
    def __init__(self):
        self.head=None

    
    def visualize(self):
        tmp=self.head
        while tmp:
            print(tmp.data,"---->",end=' ')
            tmp=tmp.next
    #Add the value in the begining
    def ATbegineg(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head =newnode
        

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
    # How to list between in the two numbers 
    def Betweeb(self,middle_node,newdata):
        if middle_node is None:
            print("No elelment to add")
            return
        newnode=Node(newdata)
        newnode.next=middle_node.next
        middle_node.next=newnode


if __name__ == "__main__":
    link=LinkdedList()
    node1=Node(10)
    node2=Node(20)
    node3=Node(40)
    link.head=node1
    link.head.next=node2
    node2.next=node3
    link.ATbegineg(2)
    link.Atend(100)
    link.Betweeb(link.head.next,200)
    link.visualize()