class RBTNode:
    def __init__(self, x: "comparable", color=None):
        self.key = x
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
class RBT():
    class EmptyTree(Exception):
        def __init__(self, data=None):
            super().__init__(data)
    class NotFound(Exception):
        def __init__(self, data=None):
            super().__init__(data)
    def __init__(self):
        self.nil = RBTNode(None, 'BLACK')
        self.root = self.nil

    def left_rotate(self, x) -> None:
        y = x.right
        x.right = y.left
        if y.left != self.nil: #self.nil is the sentinel where do i init this?
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self,x) -> None:
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def RBT_insert(self, z) -> None:
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = z.right = self.nil
        z.color = 'RED'
        self.RBT_insert_fixup(z)



    def RBT_insert_fixup(self, z) -> None:
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:
                if z.parent == z.parent.parent.right:
                    y = z.parent.parent.left
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z) # might be lrotate
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(z.parent.parent) # might be rrotate
        self.root.color = 'BLACK' 


    def RBT_transplant(self, u , v) -> None:
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def RBT_delete(self, z) -> None:
        z = self.RBT_search_iterative(self.root, z.key)
        if z == self.nil:
            raise RBT.NotFound('delete() cannot find element')
        y = z
        yOC = y.color
        if z.left == self.nil:
            x = z.right
            self.RBT_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.RBT_transplant(z, z.left)
        else:
            y = self.RBT_minimum(z.right)
            yOC = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RBT_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RBT_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if yOC == 'BLACK':
            self.RBT_delete_fixup(x)

    def RBT_delete_fixup(self, x) -> None:
        while (x != self.root and x.color == 'BLACK'):
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if (w.left.color == 'BLACK' and w.right.color == 'BLACK'):
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                if x == x.parent.right:
                    w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if (w.left.color == 'BLACK' and w.right.color == 'BLACK'):
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def RBT_minimum(self, x: RBTNode) -> RBTNode:
        if x == None:
            raise RBT.EmptyTree('minimum() invoked on empty tree')
        while x.left != self.nil:
            x = x.left
        return x

    def RBT_maximum(self, x: RBTNode) -> RBTNode:
        if x == self.nil:
            raise RBT.EmptyTree('maximum() invoked on empty tree')
        while x.right != self.nil:
            x = x.right
        return x

    def RBT_search_iterative(self, x, k) -> RBTNode:
        while x.key != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def RBT_search(self, x, k) -> RBTNode:
        z = self.RBT_search_iterative(x, k)
        if z == self.nil:
            raise RBT.NotFound('search({}) not found'.format(k))
        return z

    def inorder_helper(self, n: RBTNode, l: "list of keys") -> None:
        if n != self.nil:
            self.inorder_helper(n.left, l)
            l.append(n.key)
            self.inorder_helper(n.right, l)
    
    def to_list_inorder(self) -> "list of keys":
        l = []
        self.inorder_helper(self.root, l)
        return l

from sys import argv
def main() -> None:
    st = RBT()
    f = open(argv[1], "r")
    nl = int(f.readline().strip())
    for i in range(nl):
        l = f.readline().strip()
        if l == 'max':
            try:
                x = st.RBT_maximum(st.root)
                print(x.key)
                if x.key == None:
                    print("NONE")
            except RBT.EmptyTree as e:
                print('Empty')
        elif l == 'min':
            try:
                x = st.RBT_minimum(st.root)
                print(x.key)
            except RBT.EmptyTree as e:
                print('Empty')
        elif l == 'inprint':
            keys = st.to_list_inorder()
            if len(keys) == 0:
                print('Empty')
            else:
                strings = [str(x) for x in keys]
                print(' '.join(strings))
        else:
            v = l.split()
            if v[0] == 'insert':
                k = int(v[1])
                z = RBTNode(k)
                st.RBT_insert(z)
            elif v[0] == 'remove':
                k = int(v[1])
                try:
                    z = st.RBT_search(st.root, k)
                    st.RBT_delete(z)
                except RBT.NotFound as e:
                    print('TreeError')
            elif v[0] == 'search':
                k = int(v[1])
                try:
                    z = st.RBT_search(st.root, k)
                    print('Found')
                except RBT.NotFound as e:
                    print('NotFound')
            else:
                print("illegal input line:", l)
    f.close()

if __name__ == "__main__":
    main()
