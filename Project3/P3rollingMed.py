import sys
import math
class rollingMedList():
    def __init__(self):
        self.li = []
        self.med = 0

    def compute_med(self):
        if len(self.li) == 1:
            self.med = self.li[0]
        elif len(self.li) % 2 == 0:
            self.li.sort() # according to the documentation merge sort is used so this is O(nlogn)
            # and because it's the only calculation used it makes this nlogn time
            self.med = (self.li[math.floor((len(self.li)-1)/2)] + self.li[math.ceil((len(self.li)-1)/2)]) / 2
        else:
            self.li.sort()
            self.med = (self.li[(len(self.li)-1)//2])

def p2driver():
    medli = rollingMedList() 
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            item = int(f.readline().strip())
            medli.li.append(item)
            medli.compute_med()
            print(medli.med)

if __name__ == '__main__':
    p2driver()




