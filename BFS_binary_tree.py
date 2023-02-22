#Implement a BFS binary tree

class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None


class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if(self.items==[]):
            return None
        
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
class Binary_tree:
    def __init__(self,root):
        self.root = Node(root)

    def traversal(self):
        q = Queue()
        visit_order = []
        node = self.root
        q.enqueue(node)
        while (q.size()!=0):
            node = q.dequeue()
            visit_order.append(node.value)
            if(node.left):
                q.enqueue(node.left)
            if(node.right):
                q.enqueue(node.right)
        
        return visit_order
            
tree = Binary_tree('1')
tree.root.left = Node('2')
tree.root.right = Node('3')
tree.root.left.left = Node('4')
tree.root.left.right = Node('5')
tree.root.right.left = Node('6')
tree.root.right.right = Node('7')

print(tree.traversal())
