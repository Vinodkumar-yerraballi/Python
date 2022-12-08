class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    
def build_location_tree():
    root=TreeNode("Gobel")
    india=TreeNode("India")
    gujarat=TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahamedabadh"))
    gujarat.add_child(TreeNode("Barodh"))
    karanataka=TreeNode("Karnataka")
    karanataka.add_child(TreeNode("Bangelore"))
    karanataka.add_child(TreeNode("Mysore"))
    india.add_child(gujarat)
    india.add_child(karanataka)
    usa=TreeNode("USA")
    newjersy=TreeNode("New jersy")
    newjersy.add_child(TreeNode("Pricenton"))
    newjersy.add_child(TreeNode("Trenton"))
    california=TreeNode("Californina")
    california.add_child(TreeNode("San Francico"))
    california.add_child(TreeNode("Moutain view"))
    california.add_child(TreeNode("Palo Alto"))
    usa.add_child(newjersy)
    usa.add_child(california)
    root.add_child(india)
    root.add_child(usa)
    return root

if __name__=="__main__":
    root_node = build_location_tree()
    root_node.print_tree(1)

