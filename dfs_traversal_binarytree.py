#Implement a preorder, inorder and postorder DFS traversal for a binary tree 

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self,root):
        self.root = Node(root)

    # Root--left--right
    def preorder_traversal(self):
        visit_order = []
        node = tree.root
        
        def traverse(node):
            if (node):
                visit_order.append(node.value)
                traverse(node.left)
                traverse(node.right)
            
        traverse(node)
        
        return visit_order
    
    #left--root--right
    def inorder_traversal(tree):
        visit_order = []
        node = tree.root
        
        def traverse(node):
            if (node):
                traverse(node.left)
                visit_order.append(node.value)
                traverse(node.right)
        
        traverse(node)
        
        return (visit_order)

    # left--right--root
    def postorder_traversal(tree):
        visit_order = []
        node = tree.root
        
        def traverse(node):
            if (node):
                traverse(node.left)
                traverse(node.right)
                visit_order.append(node.value)
        
        traverse(node)
        return visit_order
                
tree = Binary_tree('1')
tree.root.left = Node('2')
tree.root.right = Node('3')
tree.root.left.left = Node('4')
tree.root.left.right = Node('5')
tree.root.right.left = Node('6')
tree.root.right.right = Node('7')

print(tree.preorder_traversal())
print(tree.inorder_traversal())
print(tree.postorder_traversal())
