class TreeNode:
    def __init__(self,name,designation):
        self.name=name
        self.designataion=designation
        self.children=[]
        self.parent=None
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent
        return level
    def print_tree(self,property_name):
        if property_name=="both":
            value=self.name + "("+self.designataion+")"
        elif  property_name=="name":
            value=self.name
        else:
            value=self.designataion
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():


    infra_head= TreeNode("vishwa","infra head")
    infra_head.add_child(TreeNode("daval","Cloud manager"))
    infra_head.add_child(TreeNode("Abijith","App manager"))
    cto=TreeNode("Chinmay","CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Amir","Application Head"))

    hr_head = TreeNode("Gels","HR Head")
    hr_head.add_child(TreeNode("Peter","recurit manager"))
    hr_head.add_child(TreeNode("Waquas","Quality manager"))

    ceo=TreeNode("Nilupul","CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo
if __name__=="__main__":
    root_node = build_product_tree()
    root_node.print_tree("name")