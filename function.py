# definition (basic concept of function)
'''
def greet():
    print("NAMASTE BHARAT")
greet()
greet()

# types of function
#(1) no argument type function
def add():
    #a,b=7,3
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    c=a+b
    print(c)
add()

#(2) argument type function
def sub(x,y):
    s=x-y
    print(s)
a = int(input("enter first number="))
b = int(input("enter second number="))

sub(a,b)
'''
#(3) argument and return vlue type function

def mul(p,q):
    d=p*q
    return d
result=mul(5,4)
print("result=",result)





