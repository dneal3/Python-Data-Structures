#problem4 MinHeap
import sys
class min_heap():

    def __init__(self):
        self.heap = []
        self.root = None

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False
    #this min heapify is an amalgum of the max-heapify found in the book and a thread from stack overflow
    #https://stackoverflow.com/questions/34964717/building-min-heap-in-python
    def min_heapify(self):
        j = 0
        for i in range(len(self.heap)):
            parent = ((i//2)) 
            if parent == 1:
                parent-=1  
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                j += 1
            if j != 0:
                self.min_heapify()

    def insert(self, x):
        self.heap.append(x)
        self.min_heapify()

    def remove(self):
        if self.is_empty() == True:
            return "HeapError"
        root = self.heap.pop(0)
        self.min_heapify()
        return root

    def look(self):
        if self.is_empty() == True:
            return "HeapError"
        return self.heap[0]

    def size(self):
        if self.is_empty() == True:
            return "Empty"
        return len(self.heap)
    
    def to_String(self):
        if self.is_empty() == True:
            return "Empty"
        stra = []
        for i in range(len(self.heap)):
            stra.append(str(self.heap[i]))
        return " ".join(stra)

        return stra
