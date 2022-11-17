'''
when a function calls itself it is called recursion
'''
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(sys.getrecursionlimit()+10000)
print(sys.getrecursionlimit())
def greet():
    global i
    print("good night",i)
    i=i+1
    greet()
i = 1
greet()