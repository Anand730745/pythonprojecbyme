'''n=148789
sum=0
while n>0:
    a=n%10
    sum=sum+a
    n=n//10
print("sum=",sum)
'''

n=150
sum=0
p=n
while n>0:
    a=n%10
    sum=sum+a*a*a
    n=n//10
print("sum",sum)


if p==sum:
    print("armstrong number")
else:
    print("not a armstrong number")



