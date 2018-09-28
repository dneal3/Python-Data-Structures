from SLLStack import Stack
import sys
def driver():
    s = Stack()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = int(value_option[0])
                s.push(value)
            elif action == "pop":
                print(s.pop())
            elif action == "print":
                print(s.print_stack())

if __name__ == "__main__":
    driver()