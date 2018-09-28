import sys
from HTTPinfo import HTTPinfo
def p1_driver():
    pq = []
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split(' ')
            addr = HTTPinfo(in_data[0], in_data[1], in_data[2])
            pq.append(addr)
        pq.sort(reverse=True) # will sort it from most important to least important then print out the tasks
        for i in pq:
            print(i.ip) # print out the task list

if __name__ == "__main__":
    p1_driver()