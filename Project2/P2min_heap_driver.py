#min_heap_driver.py
from problem4 import min_heap
import sys
def min_heap_driver():
    mh = min_heap()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                value = int(value_option[0])
                mh.insert(value)
            elif action == "remove":
                print(mh.remove())
            elif action == "print":
                print(mh.to_String())
            elif action == "best":
                print(mh.look())
            elif action == "size":
                print(mh.size())

if __name__ == "__main__":
    min_heap_driver()

