class BineaysearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BineaysearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BineaysearchTree(data)
    def search_value(self,val):
        if self.data==val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search_value(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search_value(val)
            else:
                return False
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def bulid_tree(elements):
    print("The elements in the list",elements)
    root =BineaysearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
if __name__=="__main__":
    number_tree=bulid_tree([1,4,5,7,8,9,2,222,2,2,2,2,6,6,6,7,0,8,8,12345])
    print("The tree numbers is",number_tree.in_order_traversal())
    print("The 0 in the list",number_tree.search_value(222))
    countrys=bulid_tree(["UK","India","USA","Germany","UK","Mexico"])
    print("The country in the tree",countrys.in_order_traversal())
    print("UK in the list",countrys.search_value("UK"))

