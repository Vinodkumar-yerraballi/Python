class TreeNode:
    def __init__(self,data):
        self.data=data
        self.childrean=[]
        self.parent=None
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level += 1
            p=p.parent
        return level
    def print_tree(self):
        spaces=" "* self.get_level()*3
        prefix=spaces + "|------" if self.parent else ""
        print(prefix+self.data)
        if self.childrean:
            for child in self.childrean:
                child.print_tree()

    def add_child(self,child):
        child.parent=self
        self.childrean.append(child)
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    

    

if __name__ == '__main__':
    build_product_tree()