import sys
def fact(n):
    if n==0:
        return 1
    f=n*fact(n-1)
    return f
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(sys.getrecursionlimit()+50)
#print(sys.getrecursionlimit())
print(fact(6))

