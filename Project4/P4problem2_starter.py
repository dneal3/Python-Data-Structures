class STNode:

    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None


class SyntaxTree:
    # Worked with Mariah McRae and Daniel Loyd
    # inorder tree walk is from Sventeks in class slides

    def init_helper(self, i: int, l: 'list of strings') -> STNode:
        if i >= len(l):
            return None

        node = STNode(l[i])
        node.left = self.init_helper(2 * i+1, l)
        node.right = self.init_helper(2 * i+2, l)
        return node

    def __init__(self, l: 'list of strings') -> 'complete syntax tree':
        self.root = self.init_helper(0,l)

    
    def to_list_inorder(self, n , p) -> "list of keys":
        l = ''
        if n != None:
            l += self.to_list_inorder(n.left, n)
            if p.left == n:
                l = '(' + l
            l += n.key
            l += self.to_list_inorder(n.right, n)
            if p.right == n:
                l = l +')'
        return l 

    def add_parens(self):
        li = self.to_list_inorder(self.root, self.root)
        return li

        
        

# TODO: driver function
import sys
def ST_driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        in_data = f.readline().strip().split()
        ST = SyntaxTree(in_data)
        l1 = ST.add_parens()
        print(l1)
        print(eval(l1))

if __name__ == '__main__':
    ST_driver()


                
