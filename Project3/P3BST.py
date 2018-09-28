# worked with Daniel Loyd and Mariah McRae on this project, only psuedo and stuff as usual
# most of this implemetation is from the book anyway, and post and pre order walks are from
# lecture slides. 
class BST():
    class BSTException(Exception):
        def __init__(self,data=None):
            super().__init__(data)
    
    class BSTNode():
        def __init__(self, data):
            self.parent = None
            self.lchild = None
            self.rchild = None
            self.key = data
    
    def __init__(self):
        self.root = None

    def insert(self, z): # O(h) complexity
        y = None
        x = self.root
        z = self.BSTNode(z)
        while x != None:
            y = x
            if z.key < x.key:
                x = x.lchild
            else:
                x = x.rchild
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.lchild = z
        else:
            y.rchild = z

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.lchild:
            u.parent.lchild = v
        else:
            u.parent.rchild = v
        if v != None:
            v.parent = u.parent

    def remove(self, k): # O(h) 
        if self.root == None:
            raise BST.BSTException('TreeError')
        z = self.search(self.root, k)
        if z.lchild == None:
            self.transplant(z,z.rchild)
        elif z.rchild == None:
            self.transplant(z,z.lchild)
        else:
            y = self.minimum(z.rchild)
            if y.parent != z:
                self.transplant(y, y.rchild)
                y.rchild = z.rchild
                y.rchild.parent = y
            self.transplant(z, y)
            y.lchild = z.lchild
            y.lchild.parent = y

    def search(self, x, k): # O(h) complexity
        if x == None:
            raise BST.BSTException("NotFound")
        elif k == x.key:
            return x
        elif k < x.key:
            return self.search(x.lchild, k)
        else:
            return self.search(x.rchild, k)

    def minimum(self,root): # O(h) complexity
        if self.root == None:
            raise BST.BSTException('Empty')
        while root.lchild != None:
            root = root.lchild
        return root.key

    def maximum(self, root): # O(h) complexity
        if self.root == None:
            raise BST.BSTException('Empty')
        while root.rchild != None:
            root = root.rchild
        return root.key

# Daniel Loyd and I talked about how to do this quite a bit, our solutions to how to print this
# are probably similar.
    def to_list_preorder(self, x): # O(n) complexity
        li = []
        if self.root == None:
            raise BST.BSTException('Empty')
        if x != None:
            li.append(str(x.key))
            li += self.to_list_preorder(x.lchild)
            li += self.to_list_preorder(x.rchild)
        return li

    def to_list_inorder(self, x): # O(n) complexity
        li = []
        if self.root == None:
            raise BST.BSTException('Empty')
        if x != None:
            li += self.to_list_inorder(x.lchild)
            li.append(str(x.key))
            li += self.to_list_inorder(x.rchild)
        return li

    def to_list_postorder(self, x): # O(n) complexity
        li = []
        if self.root == None:
            raise BST.BSTException('Empty')
        if x != None:
            li += self.to_list_postorder(x.lchild)
            li += self.to_list_postorder(x.rchild)
            li.append(str(x.key))
        return li

import sys
def BST_driver():
    bst = BST()
    li = []
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                value = int(value_option[0])
                bst.insert(value)
            elif action == "remove":
                try:
                    value = int(value_option[0])
                    bst.remove(value)
                except bst.BSTException as e:
                    print('TreeError')
            elif action == "search":
                try:
                    value = int(value_option[0])
                    bst.search(bst.root,value)
                    print('Found')
                except bst.BSTException as e:
                    print('NotFound')
            elif action == "preprint":
                try:
                    print(' '.join(bst.to_list_preorder(bst.root))) 
                except bst.BSTException as e:
                    print('Empty')
            elif action == "inprint":
                try:
                    print(' '.join(bst.to_list_inorder(bst.root)))
                except bst.BSTException as e:
                    print('Empty')
            elif action == "postprint":
                try:
                    print(' '.join(bst.to_list_postorder(bst.root)))
                except bst.BSTException as e:
                    print('Empty')
            elif action == "min":
                try:
                    print(bst.minimum(bst.root))
                except bst.BSTException as e:
                    print('Empty')
            elif action == "max":
                try:
                    print(bst.maximum(bst.root))
                except bst.BSTException as e:
                    print('Empty')

if __name__ == "__main__":
    BST_driver()

