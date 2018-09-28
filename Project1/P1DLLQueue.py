class Queue(object):
	'''
	Discussed this project with Mariah McRae and Daniel Loyd, no work was copied
	and only theories on how to approach the problems were shared.
	'''
    class LLNode(object):
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None #added tail to keep track of well... the tail for the FIFO functionality

    def __len__(self):
        return self.size
    
    def enqueue(self, x): # basically just an edited version of stacks push
        node = self.LLNode(x)
        if self.head != None:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1
        else:
            self.head = node
            self.tail = node
            self.size += 1

    def dequeue(self): #almost the same as stack
        if self.is_empty() == True:
            return "QueueError"
        x = self.head.data
        self.head = self.head.next
        self.size -= 1
        return x

    def is_empty(self): #same as stack
        if self.size == 0:
            return True
        else:
            return False
    
    def print_queue(s): #same as stack but not put back in reverse order
        reinsertion_list = []
        if s.is_empty() == True:
            return "Empty"
        while s.is_empty() != True:
            x = s.dequeue()
            reinsertion_list.append(str(x))
        x = " ".join(reinsertion_list)
        for i in range(len(reinsertion_list)):
            s.enqueue(int(reinsertion_list[i]))
        return x