#Problem2
#Credits to Mariah McRae, and Daniel Loyd.
import sys
#python3 problem2.py input
#https://www.programiz.com/python-programming/methods/dictionary used 
# to jog my memory of python dicts, and my driver program is basically 
# from project 1
# some code adapted from http://interactivepython.org/runestone/static/pythonds/BasicDS/SimpleBalancedParentheses.html
def bracketsDriver():
    #driver for brackets to match problem2.output given
    with open(sys.argv[1]) as f:	
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip()
            print(brackets(in_data))


def brackets(in_data):
    s = [] #list to be used as a stack
    pairs = {'{':'}', '[':']', '(':')', '<':'>'}
    #dict so I dont have to iterate through twice
    if len(in_data)%2 != 0: # quick check to see if pairs are possible
        return "NO"
    for j in range(len(in_data)): # one for loop, linear time O(n)
        openParens = pairs.keys() #shows the open parens
        closeParens = pairs.values() #shows the close parens
        if in_data[j] in openParens: 
            s.append(in_data[j]) # push it on if its an open paren
        elif in_data[j] in closeParens:
            if len(s) == 0: # if stack is empty return NO
                return "NO"
            elif pairs[s[-1]] == in_data[j]:
                # check if close paren matches most recent open paren
                s.pop() # pop it if it does
            else:
                return "NO" # no if it doesn't match anything
    return "YES"


if __name__ == '__main__':
    bracketsDriver()

