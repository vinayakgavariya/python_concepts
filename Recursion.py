# a function calling it itself
import sys

sys.setrecursionlimit(6969)
print(sys.getrecursionlimit) # limit is 1000
def greet():
    print("Hello")
    greet()  # fn being called in function itself.


