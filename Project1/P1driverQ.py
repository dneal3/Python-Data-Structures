from DLLQueue import Queue
import sys
def driver():
    s = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                s.enqueue(value)
            elif action == "dequeue":
                print(s.dequeue())
            elif action == "print":
                print(s.print_queue())

if __name__ == "__main__":
    driver()