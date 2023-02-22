# Define a search function that takes a value and returns True if a node containing that value exists in the tree, otherwise False.

class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None


class Binary_tree:
    def __init__(self,root):
        self.root = Node(root)


    def compare_node_value(self,node,new_node):
        if (node.value == new_node.value):
            return 0
        elif (new_node.value < node.value):
            return -1
        else:
            return 1
    
    def search(self,node_value):
        new_node = Node(node_value)
        node = self.root
        
        while(True):
            comparison = self.compare_node_value(node, new_node)
            if(comparison == 0):
                return True
            elif (comparison == -1):
                if (node.left):
                    node = node.left
                else:
                    return False
            else:
                if (node.right):
                    node = node.right
                else:
                    return False
        return False
                
        
tree = Binary_tree('6')
tree.root.left = Node('3')
tree.root.right = Node('7')
tree.root.left.left = Node('2')
print(tree.search('6'))
