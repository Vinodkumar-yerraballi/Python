class TreeNode:
    def __init__(self,data):
        self.data=data
        self.childrean=[]
        self.parent=None
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parenet
        return level
    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces= ' ' * self.get_level()*4
        prefix=spaces+'|___' if self.parent else " "
        print(prefix+self.data)
        if self.childrean:
            for child in self.childrean:
                child.print_tree(level)
    def add_childe(self,child):
        child.parendt=self
        self.childrean.append(child)

def build_location_tree():
    root=TreeNode("Movie")
    acoter=TreeNode("Actor")
    herion=TreeNode("Heroin")
    acoter.add_childe(TreeNode("Makup man"))
    acoter.add_childe(TreeNode("Hari style"))

    acoter.add_childe(herion)
    root.add_childe(acoter)
    root.add_childe(herion)
    return root



if __name__=="__main__":
    root_node = build_location_tree()
    root_node.print_tree(0)

    