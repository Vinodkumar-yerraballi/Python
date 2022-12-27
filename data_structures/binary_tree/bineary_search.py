class BinearySearchTree:
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
                self.left=BinearySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinearySearchTree(data)
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
    root=BinearySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=="__main__":
    number_tree=bulid_tree([1,4,5,7,8,9,2,222,2,2,2,2,6,6,6,7,0,8,8,12345])
    print("The tree numbers is",number_tree.in_order_traversal())
    print("The 0 in the list",number_tree.search_value(222))
    print("Max number",number_tree.find_max())
    print("Min number",number_tree.find_min())
    print("Sum of the elements",number_tree.calculate_sum())
    print("Pred_order_traversal",number_tree.post_order_traversal())
    print("Posr_order_traversal",number_tree.pre_order_traversal())
    


