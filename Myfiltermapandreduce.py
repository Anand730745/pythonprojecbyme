from functools import *
l=[21,32,43,45,67,78,90,13,24,35,46,57,68,79]
y=lambda n:n%2==0
v=list(filter(y,l))
print(v)

m=lambda n:n+10
print(list(map(m,v)))

m=lambda n:n-10
print(list(map(m,l)))

m=lambda n:n*10
print(list(map(m,l)))

m=lambda n:n/2
j=list(map(m,l))
print(list(map(m,l)))

g=lambda a,b:a+b

d=reduce(g,j)








