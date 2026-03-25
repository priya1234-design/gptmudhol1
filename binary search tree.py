class BSTNode:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def search(self,key):
        curNode=self.root
        while curNode is not None:
            if key==curNode.data:
                return True
            elif key<curNode.data:
                curNode=curNode.left
            else:
                curNode=curNode.right
        return False
    def delete(self,key):
        curNode=self.root
        parentNode=None
        while curNode is not None:
            if key==curNode.data:
                if temp=="Left":
                    parentNode.left=None
                else:
                    parentNode.right=None
                print(key,"Node Deleted")
                return True
            elif key<curNode.data:
                parentNode=curNode
                curNode=curNode.left
                temp="Left"
            else:
                parentNode=curNode
                curNode=curNode.right
                temp="Right"
        print(key,"Node not found")
        return False
    def insert(self,value):
        newNode=BSTNode(value)
        if self.root is None:
            self.root=newNode
        else:
            curNode=self.root
            while curNode is not None:
                if value<curNode.data:
                    if curNode.left is None:
                        curNode.left=newNode
                        break
                    else:
                        curNode=curNode.left
                else:
                    if curNode.right is None:
                        curNode.right=newNode
                        break
                    else:
                        curNode=curNode.right
    def preorder(self,rt):
        print(rt.data,end="\t")
        if rt.left is not None:
            self.preorder(rt.left)
        if rt.right is not None:
            self.preorder(rt.right)
    def inorder(self,rt):
        if rt.left is not None:
            self.inorder(rt.left)
        print(rt.data,end="\t")
        if rt.right is not None:
            self.inorder(rt.right)
    def postorder(self,rt):
        if rt.left is not None:
            self.postorder(rt.left)
        if rt.right is not None:
            self.postorder(rt.right)
        print(rt.data,end="\t")
BT=BinarySearchTree()
ls=[25,10,35,20,65,45,24]
for i in ls:
    BT.insert(i)
print("\nPre-order")
BT.preorder(BT.root)
print("\nIn-order")
BT.inorder(BT.root)
print("\nPost-order")
BT.postorder(BT.root)
print("\n35 exists:",BT.search(35))
print("65 exists:",BT.search(65))
BT.delete(75)
BT.delete(24)
print("In-order")
BT.inorder(BT.root)
print("\nPre-order")
BT.preorder(BT.root)
print("\nPost-order")
BT.postorder(BT.root)
    
