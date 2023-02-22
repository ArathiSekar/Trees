#Implement an insertion using recursion and iterative insertion of node in Binary Search Tree

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
    def __init__(self):
        self.root = None
    
    def traversal(self):
        q = Queue()
        visit_order = []
        node = self.root
        level = 0
        q.enqueue((node,level))
        while(q.size()!=0):
            node,level = q.dequeue()
            
            visit_order.append((node.value,level))
            if(node.left):
                q.enqueue((node.left,level+1))
            
            if(node.right):
                q.enqueue((node.right,level+1))
           
        return visit_order
    
    def compare_node_value(self,node,new_node):
        if (node.value == new_node.value):
            return 0
        elif (new_node.value < node.value):
            return -1
        else:
            return 1
                
    def insertion(self,node_value):
        new_node = Node(node_value)
        node = self.root
        if (self.root == None):
            self.root = new_node
            return self 
        
        while(True):
            comparison = self.compare_node_value(node, new_node)
            
            if (comparison == 0):
                #override the node. node might have left and right children, so setting as node=new_node will overwrite the left and right pointers
                node.value = new_node.value
                break
            elif (comparison == -1):
                if (node.left):
                    node = node.left
                else:
                    node.left = new_node
                    break
            else:
                if(node.right):
                    node = node.right
                else:
                    node.right = new_node
                    break
        
        return self
        
        
    def insertion_through_recursion(self, node_value):
        new_node = Node(node_value)
        node = self.root 
        
        if(self.root == None):
            self.root = new_node
            return self
            
        def insert(node, new_node):
            if(node.value == new_node.value):
                node.value = new_node.value
                        
            elif (new_node.value < node.value):
                if (node.left):
                    node = node.left
                    insert(node,new_node)
                else:
                    node.left = new_node
                        
            else:
                if(node.right):
                    node = node.right
                    insert(node, new_node)
                else:
                    node.right = new_node
                    
        insert(node,new_node)
        return self
        
tree = Binary_tree()
tree.insertion('5')
tree.insertion('6')
tree.insertion('4')
tree.insertion('2')
tree.insertion('5')
tree.insertion_through_recursion('7')
tree.insertion_through_recursion('1')
tree.insertion_through_recursion('3')
tree.insertion_through_recursion('8')
print(tree.traversal())
