class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None
class LinkdedList:
    def __init__(self):
        self.head=None
    
    def visualize(self):
        if self.head is None:
            print("The list is empty")
            return
        itr=self.head
        llter= ''
        while itr:
            llter += str(itr.data)+ "--->" if itr.next else str(itr.data)
            itr=itr.next
            print(llter)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=iter.next
        return count
    #insert the value at begning
    def insert_value_begning(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_value_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr:
            itr=itr.next
            itr=Node(data,None)
    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_value_begning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node  # type: ignore
                break

            itr = itr.next
            count += 1
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next # type: ignore
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next  # type: ignore
                break

            itr = itr.next
            count+=1
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_value_at_end(data)



if __name__ == '__main__':
    ll = LinkdedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.visualize()

    ll.insert_values([45,7,12,567,99])
    ll.insert_value_at_end(67)
    ll.visualize()