import sys
 
class Node:
    data = None
    left = None
    right = None
    def init_node(self,data):
        self.data = data
        
def insert(root, data):
    if root is None:
        new_node = Node()
        new_node.init_node(data)
        return new_node
    else:
        if data <= root.data:
            #Add the nodes in recursive manner 
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
        return root
        
#get the height in recursive manner
def height(root):
    if root is None:
        return 0
    else:
        l_height = height(root.left)
        r_height = height(root.right)
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1
            
sys.setrecursionlimit(1002)           
n = int(input())
ar = list(map(int,input().split(' ')))
root = None
for ele in ar:
    root = insert(root, ele)
 
h = height(root)
print(h)
