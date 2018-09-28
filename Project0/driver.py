from Calculator import Calculator
import sys

def driver():
    c = Calculator()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            action, x = f.readline().strip().split()
            x = int(x)
            if action == "plus":
                print(c.add(x))
            elif action == "times":
                print(c.mult(x))  # copy+paste mistake? replace with c.mult(x)
            elif action == "seen":
                response = "YES" if c.seen(x) else "NO"
                print(response)
            else:
                raise RuntimeError("INVALID INSTRUCTION")


# call with Python 3
if __name__ == "__main__":
    driver()
