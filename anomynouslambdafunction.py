# normally function code
def add(x,y):
    s=x+y
    print(s)
add(4,5)

# lambda function code

y=lambda x,y:x+y
print(y(4,6))

x=lambda n:n%2==0
print(x(9))

t=lambda a,b:a-b
print(t(5,2))

t=lambda a,b:a*b
print(t(4,5))

d=lambda a,b:a/b
print(d(50,2))


'''
the above fuction can be made anonymous
because it have only one statement 
for this we need lambda function

A lambda function can take any number of arguments, but can only have one expression.
'''








