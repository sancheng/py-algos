class Node(object):
    def __init__(self,val,parent,isleft):
        self.val = val
        self.parent = parent
        self.leftchild,self.rightchild=None,None
        if parent is not None:
            if isleft:
                parent.setleftChild(self)
            else:
                parent.setrightChild(self)

    def setleftChild(self,left):
        self.leftchild = left
        if left is not None:
            left.parent = self

    def setrightChild(self,right):
        self.rightchild = right
        if right is not None:
            right.parent = self

class AvlTree(object):
    def __init__(self,cmp_func,rootval):
        self.cmp = cmp_func
        self.root = Node(rootval,None,False)

    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.leftchild),self.height(node.rightchild))

    def insert(self,element):
        n = self.root
        #insert directly
        inode = None
        while True:
            if self.cmp(element,n.val) < 0:
                if n.leftchild is None:
                    inode = Node(element,n,True)
                    break
                else:
                    n = n.leftchild
            else:
                if n.rightchild is None:
                    inode = Node(element,n,False)
                    break
                else:
                    n = n.rightchild

        #find unbalanced subtree
        isleft_rotate = True
        path_directs = []
        while inode is not None:
            lh = self.height(inode.leftchild)
            rh = self.height(inode.rightchild)
            hdiff = lh -rh
            if hdiff > 1:
                isleft_rotate = False
                break
            elif hdiff < -1:
                break

            if inode.parent is not None:
                if inode == inode.parent.leftchild:
                    path_directs.append(0)
                else:
                    path_directs.append(1)
            inode = inode.parent



        #rebalance
        if inode is not None:
            if path_directs[-2] == 1 and path_directs[-1] == 1:
                self.left_rotate(inode.rightchild,inode)
            elif path_directs[-2] == 0 and path_directs[-1] == 0:
                self.right_rotate(inode.leftchild,inode)
            elif path_directs[-2] == 1 and path_directs[-1] == 0:
                self.left_right_rotate(inode.leftchild, inode)
            elif path_directs[-2] == 0 and path_directs[-1] == 1:
                self.right_left_rotate(inode.leftchild,inode)

    def search(self,value):
        n = self.root
        while n is not None and n.val != value:
            if n.val > value:
                n = n.leftchild
            else:
                n = n.rightchild
        return n is not None

    def left_rotate(self,node,pnode):
        pp = pnode.parent
        if pp is None:
            self.root = node
            node.parent = None
        else:
            if pp.leftchild == pnode:
                pp.setleftChild(node)
            else:
                pp.setrightChild(node)
        pnode.setrightChild(node.leftchild)
        node.setleftChild(pnode)

    def right_rotate(self,node,pnode):
        pp = pnode.parent
        if pp is None:
            self.root = node
            node.parent = None
        else:
            if pp.leftchild == pnode:
                pp.setleftChild(node)
            else:
                pp.setrightChild(node)

        pnode.setleftChild(node.rightchild)
        node.setrightChild(pnode)

    def printTree(self):
        self.printNode(self.root)

    def printNode(self,node):
        print node.val
        if node.leftchild is not None:
            self.printNode(node.leftchild)
        if node.rightchild is not None:
            self.printNode(node.rightchild)



#test right rotation
tree = AvlTree(lambda x,y:x-y,1)
tree.insert(5)
tree.insert(8)
tree.insert(10)
tree.insert(11)
tree.insert(12)
tree.printTree()
print tree.search(11)
print tree.search(7)


