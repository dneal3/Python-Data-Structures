from sys import argv
# This version of the BST is from Sventeks solution slides from project3 
# they are not mine i did however add the path finder and bpv functions
# Worked with Mariah McRae and Daniel Loyd
class BSTNode:
        def __init__(self, x: "comparable", other=None):
            self.key= x
            self.other= other
            self.left= None
            self.right= None
            self.parent= None

class BinarySearchTree:
    class EmptyTree(Exception):
        def __init__(self, data=None):
            super().__init__(data)
    class NotFound(Exception):
        def __init__(self, data=None):
            super().__init__(data)
    
    def __init__(self):
        self.root = None
    
    def insert(self, z: BSTNode) -> None:
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = z.right = None

    def search_iterative(self, x: BSTNode, k: "comparable") -> BSTNode:
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def search(self, x: BSTNode, k: "comparable") -> BSTNode:
        z = self.search_iterative(x, k)
        if z == None:
            raise BinarySearchTree.NotFound('search({}) not found'.format(k))
        return z

    def minimum(self, x: BSTNode) -> BSTNode:
        if x == None:
            raise BinarySearchTree.EmptyTree('minimum() invoked on empty tree')
        while x.left != None:
            x = x.left
        return x

    def maximum(self, x: BSTNode) -> BSTNode:
        if x == None:
            raise BinarySearchTree.EmptyTree('maximum() invoked on empty tree')
        while x.right!= None:
            x = x.right
        return x

    def transplant(self, u: BSTNode, v: BSTNode) -> None:
        if  u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left= v
        else:
            u.parent.right= v
        if v != None:
            v.parent= u.parent

    def delete(self, x: BSTNode) -> None:
        z = self.search_iterative(self.root, x.key)
        if z == None:
            raise BinarySearchTree.NotFound('delete() cannot find element')
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if  y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def preorder_helper(self, n: BSTNode, l: "list of keys") -> None:
        if n != None:
            l.append(n.key)
            self.preorder_helper(n.left, l)
            self.preorder_helper(n.right, l)

    def to_list_preorder(self) -> "list of keys":
        l = []
        self.preorder_helper(self.root, l)
        return l

    def inorder_helper(self, n: BSTNode, l: "list of keys") -> None:
        if n != None:
            self.inorder_helper(n.left, l)
            l.append(n.key)
            self.inorder_helper(n.right, l)
    
    def to_list_inorder(self) -> "list of keys":
        l = []
        self.inorder_helper(self.root, l)
        return l
    
    def postorder_helper(self, n: BSTNode, l: "list of keys") -> None:
        if n != None:
            self.postorder_helper(n.left, l)
            self.postorder_helper(n.right, l)
            l.append(n.key)
    
    def to_list_postorder(self) -> "list of keys":
        l = []
        self.postorder_helper(self.root, l)
        return l

    def best_path_value(self, root):
        if root != None:
            x =self.best_path_value(root.left)
            y =self.best_path_value(root.right)
            return max(x,y) + str(root.key).count('5')
        return 0
        

def main() -> None:
    st = BinarySearchTree()
    f = open(argv[1], "r")
    nl = int(f.readline().strip())
    for i in range(nl):
        l = f.readline().strip()
        if l == 'max':
            try:
                x = st.maximum(st.root)
                print(x.key)
            except BinarySearchTree.EmptyTree as e:
                print('Empty')
        elif l == 'min':
            try:
                x = st.minimum(st.root)
                print(x.key)
            except BinarySearchTree.EmptyTree as e:
                print('Empty')
        elif l == 'preprint':
            keys = st.to_list_preorder()
            if len(keys) == 0:
                print('Empty')
            else:
                strings = [str(x) for x in keys]
                print(' '.join(strings))
        elif l == 'inprint':
            keys = st.to_list_inorder()
            if len(keys) == 0:
                print('Empty')
            else:
                strings = [str(x) for x in keys]
                print(' '.join(strings))
        elif l == 'postprint':
            keys = st.to_list_postorder()
            if len(keys) == 0:
                print('Empty')
            else:
                strings = [str(x) for x in keys]
                print(' '.join(strings))
        elif l == 'bpv':
            if st.root == None:
                print('TreeError')
            else:
                print(st.best_path_value(st.root))
        else:
            v = l.split()
            if v[0] == 'insert':
                k = int(v[1])
                z = BSTNode(k)
                st.insert(z)
            elif v[0] == 'remove':
                k = int(v[1])
                try:
                    z = st.search(st.root, k)
                    st.delete(z)
                except BinarySearchTree.NotFound as e:
                    print('TreeError')
            elif v[0] == 'search':
                k = int(v[1])
                try:
                    z = st.search(st.root, k)
                    print('Found')
                except BinarySearchTree.NotFound as e:
                    print('NotFound')
            else:
                print("illegal input line:", l)
    f.close()

if __name__ == "__main__":
    main()
















