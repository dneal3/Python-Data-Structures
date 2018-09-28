class Stack():
    '''
    we were told in lab that it was okay to implement the LL that we were given
    in the slides so I'm just going to do that with a few tweaks of course, but
    I acknowledge the work from LLNode and some from Stack as not my own.

    Discussed this project with Mariah McRae and Daniel Loyd, no work was copied 
    and only theories on how to approach the problems were shared.
    '''
    class LLNode(object):
        def __init__(self, data=None):
            self.data = data
            self.next = None
		
    def __init__(self):
        self.size = 0
        self.head = None
		
    def __len__(self):
        return self.size
			
    def push(self, x):
        node = self.LLNode(x)
        node.next = self.head
        self.head = node
        self.size += 1
        return None
                                
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def pop(self):
        y = self.head
        if self.is_empty() == True:
            return "StackError"
        if y != None:
            self.size-=1
            self.head = self.head.next
            return y.data

    def print_stack(s):
        # only use s.push, s.pop, and s.is_empty
        reinsertion_list = []
        if s.is_empty() == True:
            return "Empty"
        while s.is_empty() != True:
            x = s.pop()
            reinsertion_list.append(str(x))
        x = " ".join(reinsertion_list)
        for i in range(len(reinsertion_list)):
            b = i+1
            s.push(int(reinsertion_list[-b]))
        return x


                        
			
