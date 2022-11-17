from math import *
a=int(input("value of first number="))
b=int(input("value of second number="))
c=int(input("value of third number="))
D=(b**2-4*a*c)


if D==0:
    print("roots are real and equal")
    x1= x2 = (-b - sqrt(D)) / (2 * a)
    print("x1=",x1,"x2=",x2)
elif D>0:
    print("roots are real and unequal ")
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("x1=",x1,"x2=",x2)
else:
    print("roots are imaginary number")
