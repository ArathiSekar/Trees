#Create a binary tree
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    
    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value = value
        
    def has_left_child(self):
        return (self.left != None)
    
    def has_right_child(self):
        return (self.right != None)
        
    def set_left_child(self,node):
        self.left = node
    
    def set_right_child(self,node):
        self.right = node
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
class Tree:
    def __init__(self,value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root
        
tree = Tree('apple')
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("pear"))

print(tree.get_root().value)
print(tree.get_root().get_right_child().value)
print(tree.get_root().get_left_child().value)
tree.get_root().get_left_child().set_left_child(Node("mango"))
print(tree.get_root().get_left_child().get_left_child().get_value())
