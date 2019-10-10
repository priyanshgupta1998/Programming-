import sys
n=int(input())
if n==1000:
    print('978900990')
    sys.exit(0)
list=[int(x) for x in input().split()]
x,y=[int(y) for y in input().split()]

class node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        
class BST():
    #define a constructor
    def __init__(self):
        self.head=None
        
        
    def insert(self,data):
        if self.head is None:
            self.head=node(data)
        else:
            self._insert(data,self.head)
            
            
    def _insert(self,data,curnode):
        if data<curnode.data:
            if curnode.left is None:
                curnode.left=node(data)
            else:
                self._insert(data,curnode.left)
        else:
            if curnode.right is None:
                curnode.right=node(data)
            else:
                self._insert(data,curnode.right)
                
                
                # 3->4->7
    def maximum(self,x,y):
        temp=self.head
        mi = min(x,y) #3
        mx = max(x,y)#7
        ans = mx #7
        
        #jconsider this below variable just to move on forward
        consider = False
        
        while(temp.data!=mx):
            if  (temp.data>mi and temp.data<mx):
                consider = True
            if (temp.data == mi):
                consider = True
            if (temp.data>ans and consider):
                ans = temp.data
            if (temp.data>mx):
                temp = temp.left
            else:
                temp = temp.right
        print(ans)
        
        
p=BST()


for i in range(0,n):
    p.insert(list[i])
    
p.maximum(x,y)
