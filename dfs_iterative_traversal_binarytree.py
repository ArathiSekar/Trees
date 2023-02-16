#Implement a binary tree preorder, inorder and postorder DFS traversal iteratively without using recursion

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if (len(self.items)==0):
            return None
        
        return self.items.pop()
    
    def size(self):
        return len(self.items)

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class Binary_tree:
    def __init__(self,root):
        self.root = Node(root)

    #Root--left--right
    def preorder_traversal(tree):
        visit_order = []
        node = tree.root
        s = Stack()
        s.push(node)
        
        while(s.size()!=0):
            node = s.pop()
            visit_order.append(node.value)
            
            if (node.right):
                s.push(node.right)
            if(node.left):
                s.push(node.left)
            
        return visit_order
    
    #left--root--right
    def inorder_traversal(tree):
        visit_order = []
        current_node = tree.root
        s = Stack()
       
        while(True):
            
            if(current_node != None):
                s.push(current_node)
                current_node = current_node.left
            elif (s.size()!=0):
                current_node = s.pop()
                visit_order.append(current_node.value)
                current_node = current_node.right
            else:
                break
        return visit_order
    
    #Left-right-root    
    def postorder_traversal(tree):
        visit_order = []
        current_node = tree.root
        s1 = Stack()
        s2 = Stack()
        s1.push(current_node)
        
        while(s1.size()!=0):
            current_node = s1.pop()
            s2.push(current_node)
            if(current_node.left):
                s1.push(current_node.left)
            if(current_node.right):
                s1.push(current_node.right)
            
        while(s2.size()!=0):
            current_node = s2.pop()
            visit_order.append(current_node.value)
    
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
