class BinearyTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return 
        if data < self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left =BinearyTreeNode(data)
        else:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right=BinearyTreeNode(data)

    def search_val(self,val):
        if self.data==val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search_val(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search_val(val)
            else:
                return False
    def in_order_transver(self):
        elements=[]
        if self.left:
            elements += self.left.in_order_transver()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_transver()
        return elements
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.left.find_max()
            self.data = min_val
            self.left = self.left.delete(min_val)

        return self

    def in_order_traversal(self):
        elements = []
        if self.left:
           elements += self.left.in_order_traversal()

        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    def pre_order_traversal(self):
        elements=[self.data]
        if self.left:
            elements +=self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        elements.append(self.data)
        return elements
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def calculate_sum(self):
        left_sum=self.left.calculate_sum() if self.left else 0
        right_sum=self.right.calculate_sum() if self.right else 0
        return self.data+left_sum+right_sum


    

def bulid_tree(elements):
    print("The elements in the list",elements)
    root=BinearyTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=="__main__":
    numbers_tree = bulid_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal())